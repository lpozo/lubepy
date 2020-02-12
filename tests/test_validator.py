#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: test_validator.py
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

"""This module provides tests for validator.py."""

import pytest
from pytest import param

from lubepy.exceptions import ValidationError, ConceptError
from lubepy.validator import (
    validate_number,
    validate_viscosity40,
    validate_viscosity100,
    validate_viscosity_index,
    validate_temperature,
)


class TestValidator:
    """Class to test Validator class."""

    @pytest.mark.parametrize(
        "name, value",
        [
            param("number", ""),
            param("number", "1.2-"),
            param("number", "invalid.string"),
            param("number", "inf"),
            param("number", "-inf"),
        ],
    )
    def test_validate_number(self, name, value):
        with pytest.raises(ValidationError):
            validate_number(name, value)

    @pytest.mark.parametrize(
        "name, value, expected",
        [
            param("number", "1.2", 1.2),
            param("number", "1,2", 1.2),
            param("number", "-1.2", -1.2),
            param("number", "- 1.2", -1.2),
            param("number", "+1.2", 1.2),
            param("number", "1 . 2 ", 1.2),
        ],
    )
    def test_validate_number_value(self, name, value, expected):
        assert validate_number(name, value) == expected

    @pytest.mark.parametrize(
        "viscosity40, expected", [param("68", 68.0), param("150", 150.0)],
    )
    def test_viscosity40(self, viscosity40, expected):
        assert validate_viscosity40(viscosity40) == expected

    @pytest.mark.parametrize(
        "viscosity40", [param("1"), param("2010")],
    )
    def test_viscosity40_wrong_value(self, viscosity40):
        with pytest.raises(ConceptError):
            validate_viscosity40(viscosity40)

    @pytest.mark.parametrize(
        "viscosity100, expected", [param("16.4", 16.4), param("15", 15.0)],
    )
    def test_viscosity100(self, viscosity100, expected):
        assert validate_viscosity100(viscosity100) == expected

    @pytest.mark.parametrize(
        "viscosity100", [param("-1"), param("501")],
    )
    def test_viscosity100_wrong_value(self, viscosity100):
        with pytest.raises(ConceptError):
            validate_viscosity100(viscosity100)

    @pytest.mark.parametrize(
        "viscosity_index, expected",
        [param("95", 95.0), param("150", 150.0), param("1", 1)],
    )
    def test_viscosity_index(self, viscosity_index, expected):
        assert validate_viscosity_index(viscosity_index) == expected

    @pytest.mark.parametrize(
        "viscosity_index", [param("-1"), param("500"), param("400.1")],
    )
    def test_viscosity_index_wrong_value(self, viscosity_index):
        with pytest.raises(ConceptError):
            validate_viscosity_index(viscosity_index)

    @pytest.mark.parametrize(
        "temp, expected", [param("-50", -50.0), param("100", 100.0), param("1200", 1200)],
    )
    def test_temperature(self, temp, expected):
        assert validate_temperature(temp) == expected

    @pytest.mark.parametrize(
        "temp", [param("-51"), param("1201"), param("3000"), param("-60")],
    )
    def test_temperature_wrong_value(self, temp):
        with pytest.raises(ConceptError):
            validate_temperature(temp)
