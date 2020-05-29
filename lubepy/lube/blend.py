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

"""This module provides the OilBlend class."""

from typing import Dict

from lubepy import MIN_OIL_DENSITY, ASH_CONTRIBUTION
from lubepy.validator.core import OilDensity, AdditivePercent, MetalContent


def additive_percent_mass(
    additive_percent: float, additive_density: float, oil_density: float
) -> float:
    """Calculate the % by mass of Additive in a motor oil."""
    return OilBlend(
        additive_percent, additive_density, oil_density, {}
    ).additive_percent_mass()


def total_ash(metal_content: dict, additive_percent: float) -> float:
    """Calculate the total content of sulfated ash."""
    return OilBlend(
        additive_percent, MIN_OIL_DENSITY, MIN_OIL_DENSITY, metal_content
    ).total_ash()


class OilBlend:
    """Class to calculate some parameters of a motor oil blend."""

    additive_percent = AdditivePercent("Additive percent")
    additive_density = OilDensity("Additive density")
    oil_density = OilDensity("Oil density")
    metal_content = MetalContent("Metal content")

    def __init__(
        self,
        additive_percent: float,
        additive_density: float,
        oil_density: float,
        metal_content: Dict[str, float],
    ) -> None:
        """Class initializer.

        additive_percent: Total % of additive in the blend (% volume)
        additive_density: Additive package density (kg/L)
        oil_density: OilDensity of the finished oil (kg/L)
        metal_content: Metallic additive content (% mass)
            e.g {'Calcium': 0.47, 'Magnesium': 1.15, 'Zinc': 1.66}
        """
        self.additive_percent = additive_percent
        self.additive_density = additive_density
        self.oil_density = oil_density
        self.metal_content = metal_content

    def additive_percent_mass(self) -> float:
        """Calculate the % by mass of Additive in a motor oil.

                                Additive OilDensity (kg/L) * Additive (% volume)
        Additive (% mass) = ---------------------------------------------------
                                       OilDensity of Finished Oil (kg/L)
        """
        return round(
            (self.additive_density * self.additive_percent) / self.oil_density,
            2,
        )

    def _ash_per_metal(self, metal: str) -> float:
        """Calculate the % of Sulfated Ash (SA) of a motor oil.

             Metal Content (%mass) * Ash Contribution * Additive Pkg (%volume)
        SA = -----------------------------------------------------------------
                                            100

        metal: Any of these: 'zinc', 'barium', 'sodium', 'calcium',
               'magnesium', 'lead', 'boron', 'potassium',
               'manganese', 'molybdenum', 'copper'
        """
        return round(
            self.metal_content[metal]
            * ASH_CONTRIBUTION[metal.lower()]
            * self.additive_percent
            / 100,
            3,
        )

    def total_ash(self) -> float:
        """Calculate the total content of sulfated ash."""
        return round(
            sum(self._ash_per_metal(metal) for metal in self.metal_content), 2
        )
