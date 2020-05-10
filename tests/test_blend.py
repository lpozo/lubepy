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

import pytest
from pytest import param

from lubepy.exceptions import ConceptError, ValidationError

from lubepy.lube.blend import (
    OilBlend,
    additive_percent_mass,
    total_ash,
)


class TestOilBlend:
    """Class to test OilBlend."""

    @pytest.mark.parametrize(
        "additive_percent, additive_density, oil_density, metal_content",
        [
            param(55.0, 0.95, 0.88, dict(Calcium=0.47, Magnesium=1.15)),
            param(0.3, 1.7, 0.88, dict(Calcium=0.47, Magnesium=1.15)),
            param(0.3, 0.9, 2, dict(Calcium=0.47, Magnesium=1.15)),
            param(0.3, 0.9, 0.88, dict(Iron=0.47)),
        ],
    )
    def test_oil_blend_concept_error(
        self, additive_percent, additive_density, oil_density, metal_content
    ):
        with pytest.raises(ConceptError):
            OilBlend(
                additive_percent, additive_density, oil_density, metal_content
            )

    @pytest.mark.parametrize(
        "additive_percent, additive_density, oil_density, metal_content",
        [
            param(float("nan"), 0.95, 0.88, dict(Calcium=0.47)),
            param(5.0, "one", 0.88, dict(Calcium=0.47, Magnesium=1.15)),
            param(5.0, ".95", None, dict(Calcium=0.47, Magnesium=1.15)),
            param(5.0, ".95", 0.88, dict(Calcium=float("nan"))),
        ],
    )
    def test_oil_blend_validation_error(
        self, additive_percent, additive_density, oil_density, metal_content
    ):
        with pytest.raises(ValidationError):
            OilBlend(
                additive_percent, additive_density, oil_density, metal_content
            )

    def test_additive_percent_mass(self):
        blend = OilBlend(
            additive_percent=8.0,
            additive_density=0.959,
            oil_density=0.881,
            metal_content=dict(Calcium=0.47, Magnesium=1.15, Zinc=1.66),
        )
        assert blend.additive_percent_mass() == 8.71

    def test_additive_percent_mass_func(self):
        assert (
            additive_percent_mass(
                additive_percent=8.0,
                additive_density=0.959,
                oil_density=0.881,
            )
            == 8.71
        )

    def test_total_ash(self):
        self.blend = OilBlend(
            additive_percent=8.5,
            additive_density=0.959,
            oil_density=0.881,
            metal_content=dict(Calcium=0.47, Magnesium=1.15, Zinc=1.66),
        )
        assert self.blend.total_ash() == 0.83

    def test_total_ash_func(self):
        assert (
            total_ash(
                metal_content=dict(Calcium=0.47, Magnesium=1.15, Zinc=1.66),
                additive_percent=8.5,
            )
            == 0.83
        )
