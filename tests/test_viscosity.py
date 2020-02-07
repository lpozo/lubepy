#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: tests_viscosity.py
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

"""This module provides tests for lubricalc package."""

from lubepy.viscosity import viscosity_at_40
from lubepy.viscosity import viscosity_at_100
from lubepy.viscosity import viscosity
from lubepy.viscosity import viscosity_index


class TestViscosity:
    """Class to test Viscosity class."""

    def test_viscosity_at_40(self):
        assert viscosity_at_40(15, index=130) == 119.55

    def test_viscosity_at_100(self):
        assert viscosity_at_100(112, index=140) == 15.11

    def test_viscosity(self):
        assert viscosity(4.6, 2, 20) == 6.89

    def test_viscosity_index(self):
        assert viscosity_index(22.83, 5.05) == 156
