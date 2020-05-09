# -*- coding: utf-8 -*-

# Copyright (C) 2020 Leodanis Pozo Ramos <lpozor78@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

"""This module provides validators for input parameters."""

from math import isinf, isnan

from lubepy import (
    LOW_VISCOSITY,
    HIGH_VISCOSITY_40,
    HIGH_VISCOSITY_100,
    LOW_INDEX,
    HIGH_INDEX,
    LOW_TEMPERATURE,
    HIGH_TEMPERATURE,
    MIN_BEARING_DIAMETER,
    MAX_BEARING_DIAMETER,
    MIN_BEARING_WIDTH,
    MAX_BEARING_WIDTH,
    MIN_RPM,
    MAX_RPM,
    MIN_DENSITY,
    MAX_DENSITY,
    MIN_ADDITIVE_PERCENT,
    MAX_ADDITIVE_PERCENT,
    ASH_CONTRIBUTION,
)

from .exceptions import ConceptError, ValidationError


def validate_viscosity(value, temperature: str) -> float:
    upper_limit = {"40": HIGH_VISCOSITY_40, "100": HIGH_VISCOSITY_100}
    validate = ParamValidator()
    return validate(
        param=f"Viscosity at {temperature}",
        value=value,
        lower=LOW_VISCOSITY,
        upper=upper_limit[temperature],
    )


def validate_viscosity_index(value) -> float:
    validate = ParamValidator()
    return validate(
        param="Viscosity Index",
        value=value,
        lower=LOW_INDEX,
        upper=HIGH_INDEX,
    )


def validate_temperature(value) -> float:
    validate = ParamValidator()
    return validate(
        param="Temperature",
        value=value,
        lower=LOW_TEMPERATURE,
        upper=HIGH_TEMPERATURE,
    )


class ParamValidator:
    """Validate params."""

    def __init__(self):
        self._param = None
        self._value = None

    def __call__(self, param, value, lower=None, upper=None):
        self._param = param
        self._value = value
        self._cleanup()
        self._to_float()
        self._check_symbols()
        self._check_range(lower, upper)
        return self._value

    def _cleanup(self):
        self._value = "".join(str(self._value).split()).replace(",", ".")

    def _to_float(self):
        try:
            self._value = float(self._value)
        except ValueError:
            raise ValidationError(self._error_msg) from None

    def _check_symbols(self):
        if isinf(self._value) or isnan(self._value):
            raise ValidationError(self._error_msg)

    def _check_range(self, lower: float = None, upper: float = None):
        if lower is None and upper is None:
            return None
        if not lower <= self._value <= upper:
            raise ConceptError(
                f"{self._param} must be between {lower} and {upper}"
            )

    @property
    def _error_msg(self):
        return f"{self._param} must be a valid number, not: {self._value}"


class BaseParam:
    def __init__(self, name):
        self._name = name
        self._value = None
        self._validate = ParamValidator()

    def __get__(self, instance, owner):
        return self._value


class Diameter(BaseParam):
    """Descriptor class for validating Bearing diameters."""

    def __set__(self, instance, value):
        self._value = self._validate(
            self._name, value, MIN_BEARING_DIAMETER, MAX_BEARING_DIAMETER
        )


class Width(BaseParam):
    """Descriptor class for validating Bearing widths."""

    def __set__(self, instance, value):
        self._value = self._validate(
            self._name, value, MIN_BEARING_WIDTH, MAX_BEARING_WIDTH
        )


class Rpm(BaseParam):
    """Descriptor class for validating Bearing rpm."""

    def __set__(self, instance, value):
        self._value = self._validate(self._name, value, MIN_RPM, MAX_RPM)


class Density(BaseParam):
    """Descriptor class for validating density."""

    def __set__(self, instance, value):
        self._value = self._validate(
            self._name, value, MIN_DENSITY, MAX_DENSITY
        )


class AdditivePercent(BaseParam):
    """Descriptor class for validating additive percent."""

    def __set__(self, instance, value):
        self._value = self._validate(
            self._name, value, MIN_ADDITIVE_PERCENT, MAX_ADDITIVE_PERCENT
        )


class MetalContent(BaseParam):
    """Descriptor class for validating metal content dict."""

    def __set__(self, instance, value):
        if isinstance(value, dict):
            self._value = {
                k.strip().lower(): self._validate(f"{self._name} for {k}", v)
                for k, v in value.items()
            }
        else:
            raise ConceptError(
                f"{self._name} must be a dictionary object not {type(value)}"
            )

        for metal in self._value:
            if metal not in ASH_CONTRIBUTION:
                raise ConceptError(f"{metal} is not a valid additive metal")
