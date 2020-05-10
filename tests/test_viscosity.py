#!/usr/bin/env python3
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

"""This module provides tests for viscosity.py."""

import pytest
from pytest import param

from lubepy.exceptions import ConceptError, ValidationError
from lubepy.lube.viscosity import (
    viscosity_at_40,
    viscosity_at_100,
    viscosity_at_any_temp,
    viscosity_index,
)


class TestViscosity:
    """Class to test Viscosity class."""

    @pytest.mark.parametrize(
        "viscosity100, index, expected",
        [
            param("15", "130", 119.55),
            param("14.5", "130", 114.1),
            param("15.2", "97", 157.9),
            param("11.8", "98", 107.7),
            param("10.5", "125", 75.45),
        ],
    )
    def test_viscosity_at_40(self, viscosity100, index, expected):
        assert viscosity_at_40(viscosity100, index) == expected

    @pytest.mark.parametrize(
        "viscosity100, index", [param("1", "100"), param("2010", "100")],
    )
    def test_viscosity_at_40_wrong_viscosity(self, viscosity100, index):
        with pytest.raises(ConceptError):
            viscosity_at_40(viscosity100, index)

    @pytest.mark.parametrize(
        "viscosity100, index", [param("16", "-30"), param("16", "401")],
    )
    def test_viscosity_at_40_wrong_index(self, viscosity100, index):
        with pytest.raises(ConceptError):
            viscosity_at_40(viscosity100, index)

    @pytest.mark.parametrize(
        "viscosity100, index",
        [
            param("", "100"),
            param("16", ""),
            param("16", float("inf")),
            param(float("-inf"), "100"),
            param("16", "string"),
            param("string", "100"),
            param(float("nan"), "100"),
        ],
    )
    def test_viscosity_at_40_wrong_value(self, viscosity100, index):
        with pytest.raises(ValidationError):
            viscosity_at_40(viscosity100, index)

    @pytest.mark.parametrize(
        "viscosity40, index, expected",
        [
            param("104.7", "133", 13.89),
            param("114.1", "130", 14.58),
            param("157.9", "97", 15.3),
            param("107.7", "98", 11.88),
            param("75.45", "125", 10.55),
        ],
    )
    def test_viscosity_at_100(self, viscosity40, index, expected):
        assert viscosity_at_100(viscosity40, index) == expected

    @pytest.mark.parametrize(
        "viscosity40, index", [param("46", "-26"), param("46", "401")],
    )
    def test_viscosity_at_100_wrong_index(self, viscosity40, index):
        with pytest.raises(ConceptError):
            viscosity_at_100(viscosity40, index)

    @pytest.mark.parametrize(
        "viscosity40, index",
        [
            param("", "100"),
            param("46", ""),
            param("46", float("inf")),
            param(float("-inf"), "100"),
            param("46", "string"),
            param("string", "100"),
            param(float("nan"), "100"),
        ],
    )
    def test_viscosity_at_100_wrong_value(self, viscosity40, index):
        with pytest.raises(ValidationError):
            viscosity_at_100(viscosity40, index)

    def test_viscosity_at_any_temp(self):
        assert viscosity_at_any_temp(4.6, 2, 20) == 6.89

    @pytest.mark.parametrize(
        "viscosity40, viscosity100, temp",
        [
            param("16", "1", "20"),
            param("1", "100", "20"),
            param("16", "100", "-60"),
        ],
    )
    def test_viscosity_at_any_temp_wrong_params(
        self, viscosity40, viscosity100, temp
    ):
        with pytest.raises(ConceptError):
            viscosity_at_any_temp(viscosity40, viscosity100, temp)

    @pytest.mark.parametrize(
        "viscosity40, viscosity100, temp",
        [
            param("16", "", "20"),
            param("", "100", "20"),
            param("16", "100", ""),
        ],
    )
    def test_viscosity_at_any_temp_wrong_number(
        self, viscosity40, viscosity100, temp
    ):
        with pytest.raises(ValidationError):
            viscosity_at_any_temp(viscosity40, viscosity100, temp)

    @pytest.mark.parametrize(
        "viscosity40, viscosity100, expected",
        [
            param("22.83", "5.05", 156),
            param("114.1", "14.58", 131),
            param("157.9", "15.3", 98),
            param("107.7", "11.88", 99),
            param("75.45", "10.55", 126),
        ],
    )
    def test_viscosity_index(self, viscosity40, viscosity100, expected):
        assert viscosity_index(viscosity40, viscosity100) == expected

    @pytest.mark.parametrize(
        "viscosity40, viscosity100",
        [param("16", "1"), param("1", "100"), param("16", "600"),],
    )
    def test_viscosity_index_wrong_params(self, viscosity40, viscosity100):
        with pytest.raises(ConceptError):
            viscosity_index(viscosity40, viscosity100)

    @pytest.mark.parametrize(
        "viscosity40, viscosity100",
        [
            param("16", ""),
            param("", "100"),
            param("string", "100"),
            param("16", float("inf")),
        ],
    )
    def test_viscosity_index_wrong_number(self, viscosity40, viscosity100):
        with pytest.raises(ValidationError):
            viscosity_index(viscosity40, viscosity100)
