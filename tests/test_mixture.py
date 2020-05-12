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

"""This module provides tests for mixture.py."""

import pytest
from pytest import param

from lubepy.exceptions import ConceptError, ValidationError
from lubepy.lube.mixture import (
    OilMixture,
    mixture_proportions,
    mixture_viscosity,
)


class TestOilMixture:
    """Class to test OilMixture class."""

    @pytest.mark.parametrize(
        """first_viscosity, second_viscosity, 
           temperature, first_oil_percent, expected""",
        [
            param(20, 16, "100", 45, 17.67),
            param(16.4, 21.5, "100", 50, 18.74),
            param(104, 95, "40", 65, 100.74),
            param(200, 158, "-5", 35, 171.39),
        ],
    )
    def test_mixture_viscosity(
        self,
        first_viscosity,
        second_viscosity,
        temperature,
        first_oil_percent,
        expected,
    ):
        """Test mixture viscosity (class API)."""
        mixture = OilMixture(first_viscosity, second_viscosity, temperature)
        assert mixture.mixture_viscosity(first_oil_percent) == expected

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

    @pytest.mark.parametrize(
        """first_viscosity, second_viscosity, 
           temperature, desired_viscosity, expected""",
        [
            param(680, 220, "40", 460, (67.32, 32.68)),
            param(680, 150, "40", 320, (53.11, 46.89)),
            param(13.9, 18.1, "100", 17.4, (14.59, 85.41)),
        ],
    )
    def test_mix_proportions(
        self,
        first_viscosity,
        second_viscosity,
        temperature,
        desired_viscosity,
        expected,
    ):
        assert (
            OilMixture(
                first_viscosity, second_viscosity, temperature
            ).mixture_proportions(desired_viscosity)
            == expected
        )

    @pytest.mark.parametrize(
        """first_viscosity, second_viscosity, 
           temperature, desired_viscosity""",
        [
            param(320, 220, "40", 460),
            param(220, 320, "40", 460),
            param(320, 460, "40", 680),
            param(14.5, 16.3, "100", 20.1),
        ],
    )
    def test_mix_proportions_wrong_interval(
        self, first_viscosity, second_viscosity, temperature, desired_viscosity
    ):
        with pytest.raises(ConceptError):
            OilMixture(
                first_viscosity, second_viscosity, temperature
            ).mixture_proportions(desired_viscosity)

    @pytest.mark.parametrize(
        """first_viscosity, second_viscosity, 
           temperature, desired_viscosity""",
        [
            param(2001, 220, "40", 460),
            param(220, 1, "40", 460),
            param(320, 460, "20", 1),
            param(14.5, 16.3, "100", 501),
        ],
    )
    def test_mix_proportions_wrong_values(
        self, first_viscosity, second_viscosity, temperature, desired_viscosity
    ):
        with pytest.raises(ConceptError):
            OilMixture(
                first_viscosity, second_viscosity, temperature
            ).mixture_proportions(desired_viscosity)

    @pytest.mark.parametrize(
        """first_viscosity, second_viscosity, 
           temperature, desired_viscosity""",
        [
            param(float("inf"), 680, "40", 460),
            param(320, "one", "40", 460),
            param(320, 680, "40", float("nan")),
        ],
    )
    def test_mix_proportions_wrong_numbers(
        self, first_viscosity, second_viscosity, temperature, desired_viscosity
    ):
        with pytest.raises(ValidationError):
            OilMixture(
                first_viscosity, second_viscosity, temperature
            ).mixture_proportions(desired_viscosity)

    def test_mix_proportions_func(self):
        assert mixture_proportions(680, 220, 460, "40") == (67.32, 32.68)
