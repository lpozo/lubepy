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
from typing import Literal

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


def validate_viscosity(value, temperature: Literal["40", "100"]) -> float:
    upper_limit = {"40": HIGH_VISCOSITY_40, "100": HIGH_VISCOSITY_100}
    viscosity = _validate_param(
        param=f"Viscosity at {temperature}",
        value=value,
        lower_limit=LOW_VISCOSITY,
        upper_limit=upper_limit[temperature],
    )
    return viscosity


def validate_viscosity_index(value) -> float:
    viscosity_index = _validate_param(
        param="Viscosity Index",
        value=value,
        lower_limit=LOW_INDEX,
        upper_limit=HIGH_INDEX,
    )
    return viscosity_index


def validate_temperature(value) -> float:
    temperature = _validate_param(
        param="Temperature",
        value=value,
        lower_limit=LOW_TEMPERATURE,
        upper_limit=HIGH_TEMPERATURE,
    )
    return temperature


def _validate_number(name: str, value) -> float:
    """Validate input and return it as float number."""
    value = "".join(str(value).split()).replace(",", ".")

    if value == "":
        value = "null"

    error_msg = f"{name} must be a valid number, not: {value}"

    try:
        result = float(value)
    except ValueError:
        raise ValidationError(error_msg) from None

    if isinf(result) or isnan(result):
        raise ValidationError(error_msg)

    return result


def _in_range(value: float, lower: float, upper: float):
    return lower <= value <= upper


def _validate_param(
    param: str, value, lower_limit: float, upper_limit: float
) -> float:
    result = _validate_number(param, value)
    if not _in_range(result, lower_limit, upper_limit):
        raise ConceptError(
            f"{param} must be between {lower_limit} and {upper_limit}"
        )
    return result
