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
        raise ValidationError(f"{name} must be a valid number, not: {value}")

    return result


def validate_viscosity40(viscosity40):
    return _validate_range("viscosity40", viscosity40, LOW_VISCOSITY, HIGH_VISCOSITY_40)


def validate_viscosity100(viscosity100):
    return _validate_range(
        "viscosity100", viscosity100, LOW_VISCOSITY, HIGH_VISCOSITY_100
    )


def validate_viscosity_index(viscosity_index):
    return _validate_range("viscosity_index", viscosity_index, LOW_INDEX, HIGH_INDEX)


def _validate_range(name, value, lower, upper):
    result = validate_number(name, value)
    if not (lower <= result <= upper):
        raise ConceptError(f"{name} must be between {lower} and {upper}")
    return result


class ValidNumber:
    """Descriptor for representing numerical values."""

    def __init__(self, name: str) -> None:
        self._value: float
        self._name = name

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        """Validate input value as float."""
        self._value = validate_number(self._name, value)


class NonZeroPositiveNumber(ValidNumber):
    """Descriptor for representing non-zero positive numbers."""

    def __set__(self, instance, value):
        """Validate input value as float."""
        self._value = validate_number(self._name, value)
        if self._value <= 0:
            raise ValidationError("Input value must be greater than 0")


# class Validator:
#     """Data validation class."""

#     @staticmethod
#     def validate_lower_limit(name, value, limit=0, strict=False):
#         """Validate value is greater than a given value (limit)."""
#         if not strict:
#             if value < limit:
#                 raise ConceptError(
#                     "{0}: Input value must be "
#                     "greater than or equal to {1}".format(name, limit)
#                 )
#         else:
#             if value <= limit:
#                 raise ConceptError(
#                     "{0}: Input value must be " "greater than {1}".format(name, limit)
#                 )


# def validate(obj, name, value, attr, limit=0, strict=False):
#     """Validate and set attributes of an object."""
#     validator = Validator()
#     value = validator.validate_float(name, value)
#     lower_limit = limit
#     validator.validate_lower_limit(name, value, lower_limit, strict)
#     setattr(obj, attr, value)

# class Temperature:
#     """Descriptor for representing non-zero positive values."""

#     def __get__(self, instance, owner):
#         return self._temperature

#     def __set__(self, instance, value):
#         self.__temperature = value
#         if self.__temperature >= -50:
#             self._temperature = self.__temperature
#         else:
#             raise ConceptError("Temperature must be greater -50°C")

#     __temperature = Float()
