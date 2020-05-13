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

"""This module provides the Reynold number calculations."""

from enum import Enum


def reynolds_circular_session(
    velocity: float, viscosity: float, diameter: float
) -> float:
    """Calculate Reynolds number (Re)."""
    return ReynoldsNumber(velocity, viscosity).reynolds_circular_session(
        diameter
    )


def reynolds_square_session(
    velocity: float, viscosity: float, side: float
) -> float:
    """Calculate Reynolds number (Re)."""
    return ReynoldsNumber(velocity, viscosity).reynolds_square_session(side)


def reynolds_rectangular_session(
    velocity: float, viscosity: float, base: float, height: float
) -> float:
    """Calculate Reynolds number (Re)."""
    return ReynoldsNumber(velocity, viscosity).reynolds_rectangular_session(
        base, height
    )


def flow_type_circular_session(
    velocity: float, viscosity: float, diameter: float
) -> str:
    """Determine the flow type of a fluid."""
    return FluidFlowType(velocity, viscosity).flow_type_circular_session(
        diameter
    )


def flow_type_square_session(
    velocity: float, viscosity: float, side: float
) -> str:
    """Determine the flow type of a fluid."""
    return FluidFlowType(velocity, viscosity).flow_type_square_session(side)


def flow_type_rectangular_session(
    velocity: float, viscosity: float, base: float, height: float
) -> str:
    """Determine the flow type of a fluid."""
    return FluidFlowType(velocity, viscosity).flow_type_rectangular_session(
        base, height
    )


class ReynoldsNumber:
    """Class for calculations related to Reynolds number."""

    def __init__(self, velocity: float, viscosity: float) -> None:
        self.velocity = velocity
        self.viscosity = viscosity

    def _reynolds_number(self, length) -> float:
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
        return round(self.velocity * length / self.viscosity, 1)

    def reynolds_circular_session(self, diameter):
        return self._reynolds_number(length=diameter)

    def reynolds_square_session(self, side):
        return self._reynolds_number(length=side)

    def reynolds_rectangular_session(self, base, height):
        return self._reynolds_number(
            length=(2 * base * height) / (base + height)
        )


class _FlowTypes(Enum):
    """Enumeration to represent the flow type."""

    LAMINAR: str = "laminar"
    TURBULENT: str = "turbulent"
    MIXED: str = "mixed"


class FluidFlowType:
    def __init__(self, velocity, viscosity):
        self._velocity = velocity
        self._viscosity = viscosity
        self._reynolds_number = ReynoldsNumber(self._velocity, self._viscosity)

    @staticmethod
    def _flow_type(number: float) -> _FlowTypes:
        """Determine the flow type of a fluid.

        Re < 2000 => Laminar flow
        2000.0 < reynolds < 4000.0 => Mixed flow
        Re > 4000 => Turbulent flow
        """
        if number <= 2_000.0:
            return _FlowTypes.LAMINAR
        if number >= 4_000.0:
            return _FlowTypes.TURBULENT

        return _FlowTypes.MIXED

    def flow_type_circular_session(self, diameter):
        number = self._reynolds_number.reynolds_circular_session(diameter)
        return self._flow_type(number)

    def flow_type_square_session(self, side):
        number = self._reynolds_number.reynolds_square_session(side)
        return self._flow_type(number)

    def flow_type_rectangular_session(self, base, height):
        number = self._reynolds_number.reynolds_rectangular_session(
            base, height
        )
        return self._flow_type(number)
