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

"""This module provides tests for bearing.py."""

import pytest
from pytest import param

from lubepy import MIN_BEARING_DIAMETER
from lubepy.bearing import (
    Bearing,
    grace_amount,
    lubrication_frequency,
    velocity_factor,
)
from lubepy.exceptions import ConceptError
from lubepy.exceptions import ValidationError


class TestBearing:
    """Class to test Bearing class."""

    @pytest.mark.parametrize(
        "outer, inner, width",
        [
            param(20, 40, 1),
            param(0, 40, 1),
            param(60, 40, -5),
            param(60, 0, 1),
            param("0", "40", "1"),
        ],
    )
    def test_bearing_class(self, outer, inner, width):
        with pytest.raises(ConceptError):
            Bearing(outer, inner, width)

    @pytest.mark.parametrize(
        "outer, inner, width",
        [
            param("", 40, 1),
            param(60, "", 1),
            param(60, 40, ""),
            param(60, 40, float("inf")),
            param(60, float("nan"), 1),
        ],
    )
    def test_bearing_class_wrong_number(self, outer, inner, width):
        with pytest.raises(ValidationError):
            Bearing(outer, inner, width)

    @pytest.mark.parametrize(
        "outer_diameter, width, expected",
        [param(25, 60, 7.5), param("25", "60", 7.5)],
    )
    def test_grease_amount(self, outer_diameter, width, expected):
        """Test grease_amount()."""
        bearing = Bearing(outer_diameter, MIN_BEARING_DIAMETER, width)
        assert bearing.grease_amount() == expected

    @pytest.mark.parametrize(
        "outer_diameter, width, expected", [param(25, 60, 7.5)]
    )
    def test_grace_amount_func(self, outer_diameter, width, expected):
        assert grace_amount(outer_diameter, width) == expected

    def test_lubrication_frequency(self):
        """Test lubrication_frequency()."""
        bearing = Bearing(40, 20, 1)
        assert (
            bearing.lubrication_frequency(
                rpm=1750.0, factors=dict(ft=0, fc=1, fh=2, fv=0, fp=0, fd=2)
            )
            == 478
        )

    def test_lubrication_frequency_func(self):
        """Test lubrication_frequency()."""
        assert (
            lubrication_frequency(
                inner_diameter=20,
                rpm=1750.0,
                factors=dict(ft=0, fc=1, fh=2, fv=0, fp=0, fd=2),
            )
            == 478
        )

    def test_velocity_factor(self):
        """Test speed_factor()."""
        bearing = Bearing(58, 45, 1)
        assert bearing.velocity_factor(3000) == 154500

    def test_velocity_factor_func(self):
        """Test speed_factor()."""
        assert velocity_factor(58, 45, 3000) == 154500
