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

from lubepy.bearing import (
    Bearing,
    grace_amount,
    lubrication_frequency,
    velocity_factor,
)
from lubepy.exceptions import ConceptError


class TestBearing:
    """Class to test Bearing class."""

    def test_bearing_class(self):
        with pytest.raises(ConceptError):
            Bearing(20, 40, 1)

    @pytest.mark.parametrize(
        "outer_diameter, width, expected", [(25, 60, 7.5)]
    )
    def test_grease_amount(self, outer_diameter, width, expected):
        """Test grease_amount()."""
        bearing = Bearing(outer_diameter, outer_diameter / 2, width)
        assert bearing.grease_amount() == expected

    @pytest.mark.parametrize(
        "outer_diameter, width, expected", [(25, 60, 7.5)]
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
