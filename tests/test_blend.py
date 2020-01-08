#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: test_blend.py
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

"""This module provides tests for blend.py."""

from lubepy.blend import OilBlend


class TestOilBlend:
    """Class to test OilBlend."""

    def setup(self):
        self.blend = OilBlend(8.0, 0.959, 0.881, 0.0)

    def test_additive_percent_mass(self):
        assert self.blend.additive_percent_mass() == 8.71

    # def test_total_ash(self):
    #     blend = OilBlend(additive_percent=8.5)
    #     assert blend.total_ash(Calcium=0.47,
    #                            Magnesium=1.15,
    #                            zinc=1.66) == 0.83

    # def test_total_ash_string_input(self):
    #     blend = OilBlend(additive_percent='8.5 ')
    #     assert blend.total_ash(Calcium='.47',
    #                            Magnesium=' 1,15',
    #                            zinc=1.66) == 0.83
