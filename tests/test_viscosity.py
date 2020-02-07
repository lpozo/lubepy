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


class TestViscosity:
    """Class to test Viscosity class."""

    def test_viscosity_at_40(self):
        assert viscosity_at_40(15, index=130) == 119.55

    # def test_viscosity_index_156(self):
    #     assert Viscosity().viscosity_index(22.83, 5.05) == 156

    # def test_viscosity_index_92(self):
    #     assert Viscosity().viscosity_index(73.3, 8.86) == 92

    # def test_viscosity_index_145(self):
    #     assert Viscosity().viscosity_index(138.9, 18.1) == 145

    # def test_viscosity_index_string_input(self):
    #     assert Viscosity().viscosity_index('138.9', '18.1') == 145

    # def test_viscosity_index_coma_input(self):
    #     assert Viscosity().viscosity_index('138,9', '18,1') == 145

    # @nose.tools.raises(ValueError)
    # def test_viscosity_index_inf_input(self):
    #     Viscosity().viscosity_index(float('inf'), '18,1')

    # @nose.tools.raises(ConceptError)
    # def test_viscosity_index_cero_kv40_input(self):
    #     Viscosity().viscosity_index(0, '18,1')

    # @nose.tools.raises(ConceptError)
    # def test_viscosity_index_cero_kv100_input(self):
    #     Viscosity().viscosity_index(150, 0)

    # @nose.tools.raises(InvertedViscosityError)
    # def test_viscosity_index_kv40_lt_kv100_input(self):
    #     Viscosity().viscosity_index(15, 150)

    # @nose.tools.raises(ConceptError)
    # def test_viscosity_index_input_lt_2(self):
    #     Viscosity().viscosity_index(1.5, 1)

    # def test_viscosity_at_100(self):
    #     assert Viscosity().viscosity_at_100(112, v_index=140) == 15.12

    # def test_viscosity_at_20_iso5(self):
    #     assert Viscosity().viscosity_at_any_temp(4.6, 2, 20) == 6.89

    # def test_viscosity_at_20_iso46(self):
    #     assert Viscosity().viscosity_at_any_temp(46, 7, 20) == 130.66

    # def test_viscosity_at_35_iso46(self):
    #     assert Viscosity().viscosity_at_any_temp(46, 7, 35.0) == 58.08

    # def test_viscosity_at_35_iso46_string_input(self):
    #     assert Viscosity().viscosity_at_any_temp('46', '7 ', '35.0') == 58.08

    # @nose.tools.raises(ConceptError)
    # def test_viscosity_lt_273_iso46(self):
    #     Viscosity().viscosity_at_any_temp('46', '7 ', '-275')
