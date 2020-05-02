# -*- coding: utf-8 -*-

# File name: lubricalc.py
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

"""This module provides Reynolds' number calculations."""

from enum import Enum


class FlowType(Enum):
    """Enumeration to represent the flow type."""

    LAMINAR: str = "laminar"
    TURBULENT: str = "turbulent"
    MIXED: str = "mixed"


def reynolds_number(velocity: float, length: float, viscosity: float) -> float:
    """Calculate Reynolds number (Re)."""
    return Reynolds(velocity, length, viscosity).reynolds_number()


def flow_type(velocity: float, length: float, viscosity: float) -> FlowType:
    """Determine the flow type of a fluid."""
    return Reynolds(velocity, length, viscosity).flow_type()


class Reynolds:
    """Class for calculations related to Reynolds number."""

    def __init__(
        self, velocity: float, length: float, viscosity: float
    ) -> None:
        self.velocity = velocity
        self.length = length
        self.viscosity = viscosity

    def reynolds_number(self) -> float:
        """Calculate Reynolds number (Re).

              V * Lc
        Re = --------  [(m/s m) / m^2/s]
                v
        where:
            V: velocity (m/s)
            Lc: characteristic length (m)
                For circular session Lc = D
                    D: diameter
                For square session Lc = L
                    L: side
                                             (2 * a * b)
                For rectangular session Lc = -----------
                                               (a + b)
                    a, b: sides
            v: Kinematic Viscosity (m^2/s)
        """
        return round(self.velocity * self.length / self.viscosity, 1)

    def flow_type(self) -> FlowType:
        """Determine the flow type of a fluid.

        Re < 2000 => Laminar flow
        2000.0 < reynolds < 4000.0 => Mixed flow
        Re > 4000 => Turbulent flow
        """
        reynolds = self.reynolds_number()
        if reynolds <= 2000.0:
            return FlowType.LAMINAR
        if reynolds >= 4000.0:
            return FlowType.TURBULENT

        return FlowType.MIXED
