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

ASH_CONTRIB = {
    "zinc": 1.50,
    "barium": 1.70,
    "sodium": 3.09,
    "calcium": 3.40,
    "magnesium": 4.95,
    "lead": 1.464,
    "boron": 3.22,
    "potassium": 2.23,
    "manganese": 1.291,
    "molybdenum": 1.5,
    "copper": 1.252,
}


def additive_percent_mass(
    additive_percent: float, additive_density: float, oil_density: float
) -> float:
    """Calculate the % by mass of Additive in a motor oil."""
    return OilBlend(
        additive_percent, additive_density, oil_density, {}
    ).additive_percent_mass()


def ash_per_metal(
    metal: str, metal_content: Dict[str, float], additive_percent: float
) -> float:
    """Calculate the % of Sulfated Ash (SA) of a motor oil."""
    return OilBlend(additive_percent, 0.0, 0.0, metal_content).ash_per_metal(
        metal
    )


def total_ash(metal_content: dict, additive_percent: float) -> float:
    """Calculate the total content of sulfated ash."""
    return OilBlend(additive_percent, 0.0, 0.0, metal_content).total_ash()


class OilBlend:
    """Class to calculate some parameters of a motor oil blend."""

    ash_contrib: dict = ASH_CONTRIB

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
        oil_density: Density of the finished oil (kg/L)
        metal_content: Metallic additive content (% mass)
            e.g {'Calcium': 0.47, 'Magnesium': 1.15, 'Zinc': 1.66}
        """
        self.additive_percent = additive_percent
        self.additive_density = additive_density
        self.oil_density = oil_density
        self.metal_content = metal_content

    def additive_percent_mass(self) -> float:
        """Calculate the % by mass of Additive in a motor oil.

                                Additive Density (kg/L) * Additive (% volume)
        Additive (% mass) = ---------------------------------------------------
                                       Density of Finished Oil (kg/L)
        """
        return round(
            (self.additive_density * self.additive_percent) / self.oil_density,
            2,
        )

    def ash_per_metal(self, metal: str) -> float:
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
            * self.ash_contrib[metal.lower()]
            * self.additive_percent
            / 100,
            3,
        )

    def total_ash(self) -> float:
        """Calculate the total content of sulfated ash."""
        return round(
            sum(self.ash_per_metal(metal) for metal in self.metal_content), 2
        )
