# -*- coding: utf-8 -*-

# File name: bearing.py
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

"""This module provides Bearing Class."""

import math


def grace_amount(outer_diameter: float, width: float) -> float:
    """Return the amount of grease (g) needed for re-lubrication."""
    return Bearing(outer_diameter, 0.0, width).grease_amount()


def lubrication_frequency(inner_diameter: float,
                          rpm: float,
                          **factors: dict) -> float:
    """Return the amount of grease (g) needed for re-lubrication."""
    bearing = Bearing(0.0, inner_diameter, 0.0)
    return bearing.lubrication_frequency(rpm, **factors)


def velocity_factor(outer_diameter: float,
                    inner_diameter: float,
                    rpm: float) -> float:
    """Calculate the velocity factor of a bearing."""
    bearing = Bearing(outer_diameter, inner_diameter, 0.0)
    return bearing.velocity_factor(rpm)


class Bearing:
    """Class to define calculations related with bearings."""

    def __init__(self,
                 outer_diameter: float,
                 inner_diameter: float,
                 width: float):
        """Class initializer."""
        self.outer_diameter = outer_diameter
        self.inner_diameter = inner_diameter
        self.width = width

    def grease_amount(self) -> float:
        """Return the amount of grease (g) needed for re-lubrication.

        Gg = 0.005 * D * B
        where:
        Gg: Amount of grease needed for re-lubrication (g)
        D: Outer diameter of bearing (mm)
        B: Total width of bearing (mm)
        """
        unit_coefficient = 0.005

        return round(unit_coefficient * self.outer_diameter * self.width, 2)

    def lubrication_frequency(self, rpm: float, **factors: dict) -> float:
        """Calculate the re-lubrication frequency in hours.

                       14000000
        T = K * [(------------------) - 4 * d]
                      n * sqrt(d)

        where:
        T: Frequency of re-lubrication (hours)
        K: Corrections factors
            K = Ft * Fc * Fh * Fv * Fp * Fd
            where:
            Ft: Temperature of bearing housing factor
                < 65°C, then Ft = 1.0
                65 to 80°C, then Ft = 0.5
                80 to 93°C, then Ft = 0.2
                > 93°C, then Ft = 0.1
            Fc: Solid contamination factor
                Light, no abrasive dust, then Fc = 1.0
                Severe, no abrasive dust, then Fc = 0.7
                Light, abrasive dust, then Fc = 0.4
                Severe, abrasive dust, then Fc = 0.2
            Fh: Moisture factor
                < 80 % ,then Fh = 1.0
                80 to 90 %, then Fh = 0.7
                Occasional condensation, then Fh = 0.4
                Water, then Fh = 0.2
            Fv: Vibrations factor
                Top velocity < 0.5 cm/s, then Fv = 1.0
                0.5 to 1.0 cm/s, then Fv = 0.6
                > 1.0 cm/s, then Fv = 0.3
            Fp: Shaft position factor
                Horizontal, then Fp = 1.0
                45 degrees, then Fp = 0.5
                Vertical, then Fp = 0.3
            Fd: Bearing design factor
                Ball bearing, then Fd = 10
                Cylinder/Needle roller bearing, then Fd = 5
                Conical roller bearing, then Fd = 1
        n: Rotation velocity (rpm)
        d: Inner diameter of the bearing (mm)
        """

        factors_map = {'ft': (1.0, 0.5, 0.2, 0.1),
                       'fc': (1.0, 0.7, 0.4, 0.2),
                       'fh': (1.0, 0.7, 0.4, 0.1),
                       'fv': (1.0, 0.6, 0.3),
                       'fp': (1.0, 0.5, 0.3),
                       'fd': (10.0, 5.0, 1.0)}

        k_factor = 1

        for factor, score_index in factors.items():
            k_factor *= factors_map[factor][int(score_index)]

        frequency = k_factor * ((14000000 /
                                 (rpm * math.sqrt(self.inner_diameter))) -
                                4 * self.inner_diameter)

        return round(frequency)

    def velocity_factor(self, rpm):
        """Calculate the velocity factor of a bearing.

        A = n * dm
        where:
        A: Velocity factor (mm/min)
        n: Rotation velocity (rpm)
        dm: Mean diameter (mm)
               (D + d)
        dm = -----------
                  2
        """

        return round(rpm * (self.outer_diameter + self.inner_diameter) / 2)
