# -*- coding: utf-8 -*-

# File name: validator.py
#
# Copyright (C) 2018 Leodanis Pozo Ramos <lpozor78@gmail.com>
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

"""This module provides validators."""

from lubepy import (
    LOW_VISCOSITY,
    HIGH_VISCOSITY_40,
    HIGH_VISCOSITY_100,
    LOW_INDEX,
    HIGH_INDEX,
    LOW_TEMPERATURE,
    HIGH_TEMPERATURE,
)

from .exceptions import ConceptError, ValidationError


def validate_number(name: str, value: str) -> float:
    """Validate input and return it as float number."""
    value = "".join(str(value).split()).replace(",", ".")
    try:
        result = float(value)
        if result in {float("-inf"), float("inf")}:
            raise ValueError
    except ValueError:
        if value == "":
            value = "null"
        raise ValidationError(
            f"{name} must be a valid number, not: {value}"
        ) from None

    return result


def validate_viscosity40(viscosity40):
    return _validate_range(
        "viscosity40", viscosity40, LOW_VISCOSITY, HIGH_VISCOSITY_40
    )


def validate_viscosity100(viscosity100):
    return _validate_range(
        "viscosity100", viscosity100, LOW_VISCOSITY, HIGH_VISCOSITY_100
    )


def validate_viscosity_index(viscosity_index):
    return _validate_range(
        "viscosity_index", viscosity_index, LOW_INDEX, HIGH_INDEX
    )


def validate_temperature(temperature):
    return _validate_range(
        "temperature", temperature, LOW_TEMPERATURE, HIGH_TEMPERATURE
    )


def _validate_range(name, value, lower, upper):
    result = validate_number(name, value)
    if not (lower <= result <= upper):
        raise ConceptError(f"{name} must be between {lower} and {upper}")
    return result
