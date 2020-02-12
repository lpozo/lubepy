#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: tests_mixture.py
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

"""This module provides tests for mixture.py."""

import pytest

from lubepy.exceptions import ConceptError
from lubepy.mixture import OilMixture, mixture_proportions, mixture_viscosity


class TestOilMixture:
    """Class to test OilMixture class."""

    def test_mixture_viscosity(self):
        """Test mixture viscosity (class API)."""
        mixture = OilMixture(first_viscosity=20, second_viscosity=16)
        assert mixture.mixture_viscosity(45, "100") == 17.67

    def test_mixture_viscosity_func(self):
        """Test mixture viscosity (func API)."""
        assert (
            mixture_viscosity(
                first_viscosity=20,
                first_oil_percent=45,
                second_viscosity=16,
                temperature="100",
            )
            == 17.67
        )

    def test_mix_proportions(self):
        assert OilMixture(680, 220).mixture_proportions(460, "40") == (67.32, 32.68)

    def test_mix_proportions_wrong_interval(self):
        with pytest.raises(ConceptError):
            OilMixture(320, 220).mixture_proportions(460, "40")

    def test_mix_proportions_func(self):
        assert mixture_proportions(680, 220, 460, "40") == (67.32, 32.68)
