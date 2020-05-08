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

"""This module provides tests for blend.py."""

from lubepy.blend import (
    OilBlend,
    additive_percent_mass,
    ash_per_metal,
    total_ash,
)


class TestOilBlend:
    """Class to test OilBlend."""

    def setup_method(self):
        self.blend = OilBlend(
            additive_percent=8.0,
            additive_density=0.959,
            oil_density=0.881,
            metal_content=dict(Calcium=0.47, Magnesium=1.15, Zinc=1.66),
        )

    def test_additive_percent_mass(self):
        assert self.blend.additive_percent_mass() == 8.71

    def test_additive_percent_mass_func(self):
        assert (
            additive_percent_mass(
                additive_percent=8.0,
                additive_density=0.959,
                oil_density=0.881,
            )
            == 8.71
        )

    def test_ash_per_metal(self):
        assert self.blend.ash_per_metal("Calcium") == 0.128

    def test_ash_per_metal_func(self):
        assert (
            ash_per_metal(
                "Calcium",
                metal_content=dict(Calcium=0.47),
                additive_percent=8.0,
            )
            == 0.128
        )

    def test_total_ash(self):
        self.blend.additive_percent = 8.5
        assert self.blend.total_ash() == 0.83

    def test_total_ash_func(self):
        assert (
            total_ash(
                metal_content=dict(Calcium=0.47, Magnesium=1.15, Zinc=1.66),
                additive_percent=8.5,
            )
            == 0.83
        )
