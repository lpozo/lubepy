#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: test_bearing.py
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

"""This module provides tests for bearing.py."""

import pytest

from lubepy import bearing


class TestBearing:
    """Class to test Bearing class."""

    def setup(self):
        self.bearing = bearing.Bearing(0.0, 0.0, 0.0)

    @pytest.mark.parametrize(
        "outer_diameter, width, expected",
        [(25, 60, 7.5)])
    def test_grease_amount(self, outer_diameter, width, expected):
        """Test grease_amount()."""
        self.bearing.outer_diameter = outer_diameter
        self.bearing.width = width
        assert self.bearing.grease_amount() == expected

    @pytest.mark.parametrize(
        "outer_diameter, width, expected",
        [(25, 60, 7.5)])
    def test_grace_amount_func(self, outer_diameter, width, expected):
        assert bearing.grace_amount(outer_diameter, width) == expected

    def test_lubrication_frequency(self):
        """Test lubrication_frequency()."""
        self.bearing.inner_diameter = 20
        assert self.bearing.lubrication_frequency(rpm=1750.0,
                                                  ft=0,
                                                  fc=1,
                                                  fh=2,
                                                  fv=0,
                                                  fp=0,
                                                  fd=2) == 478

    def test_lubrication_frequency_func(self):
        """Test lubrication_frequency()."""
        assert bearing.lubrication_frequency(inner_diameter=20,
                                             rpm=1750.0,
                                             ft=0,
                                             fc=1,
                                             fh=2,
                                             fv=0,
                                             fp=0,
                                             fd=2) == 478

    def test_velocity_factor(self):
        """Test speed_factor()."""
        self.bearing.outer_diameter = 58
        self.bearing.inner_diameter = 45
        assert self.bearing.velocity_factor(3000) == 154500

    def test_velocity_factor_func(self):
        """Test speed_factor()."""
        assert bearing.velocity_factor(58, 45, 3000) == 154500
