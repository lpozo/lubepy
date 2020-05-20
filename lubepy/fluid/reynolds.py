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

from lubepy.validator.core import (
    FlowRate,
    PipeSession,
)
from lubepy import MIN_PIPE_EQUIVALENT_DIAMETER
from lubepy.lube.viscosity import viscosity_at_any_temp
from lubepy.validator.core import ParamValidator


def reynolds_circular_session(
    flow_rate: float,
    viscosity40: float,
    viscosity100: float,
    temperature: float,
    diameter: float,
) -> float:
    """Calculate Reynolds number (Re)."""
    return ReynoldsNumber(
        flow_rate, viscosity40, viscosity100, temperature
    ).reynolds_circular_session(diameter)


def reynolds_square_session(
    velocity: float,
    viscosity40: float,
    viscosity100: float,
    temperature: float,
    side: float,
) -> float:
    """Calculate Reynolds number (Re)."""
    return ReynoldsNumber(
        velocity, viscosity40, viscosity100, temperature
    ).reynolds_square_session(side)


def reynolds_rectangular_session(
    velocity: float,
    viscosity40: float,
    viscosity100: float,
    temperature: float,
    base: float,
    height: float,
) -> float:
    """Calculate Reynolds number (Re)."""
    return ReynoldsNumber(
        velocity, viscosity40, viscosity100, temperature
    ).reynolds_rectangular_session(base, height)


def flow_type_circular_session(
    velocity: float,
    viscosity40: float,
    viscosity100: float,
    temperature: float,
    diameter: float,
) -> str:
    """Determine the flow type of a fluid."""
    return FluidFlowType(
        velocity, viscosity40, viscosity100, temperature
    ).flow_type_circular_session(diameter)


def flow_type_square_session(
    velocity: float,
    viscosity40: float,
    viscosity100: float,
    temperature: float,
    side: float,
) -> str:
    """Determine the flow type of a fluid."""
    return FluidFlowType(
        velocity, viscosity40, viscosity100, temperature
    ).flow_type_square_session(side)


def flow_type_rectangular_session(
    velocity: float,
    viscosity40: float,
    viscosity100: float,
    temperature: float,
    base: float,
    height: float,
) -> str:
    """Determine the flow type of a fluid."""
    return FluidFlowType(
        velocity, viscosity40, viscosity100, temperature
    ).flow_type_rectangular_session(base, height)


class ReynoldsNumber:
    """Class for calculations related to Reynolds number."""

    _flow_rate = FlowRate("Flow rate")
    _equivalent_diameter = PipeSession("Pipe equivalent diameter")

    def __init__(
        self,
        flow_rate: float,
        viscosity40: float,
        viscosity100: float,
        temperature: float,
    ) -> None:
        self._flow_rate = flow_rate
        self._viscosity = viscosity_at_any_temp(
            viscosity40, viscosity100, temperature
        )
        self._equivalent_diameter = MIN_PIPE_EQUIVALENT_DIAMETER

    def _reynolds_number(self, equivalent_diameter: float) -> float:
        """Calculate Reynolds number (Re).

              K * Q
        Re = --------  => non-unit
              Lc * v
        where:
            K: Conversion factor = 353.9606
            Q: Flow rate (L/h)
            Lc: characteristic length (mm)
                For circular session Lc = D
                    D: diameter
                For square session Lc = L
                    L: side
                                             (2 * a * b)
                For rectangular session Lc = -----------
                                               (a + b)
                    a, b: sides
            v: Kinematic Viscosity (cSt)
        """
        K = 353.9606
        self._equivalent_diameter = equivalent_diameter

        return round(
            (K * self._flow_rate)
            / (self._equivalent_diameter * self._viscosity),
            1,
        )

    def _reynolds_circular_square(self, equivalent_diameter):
        return self._reynolds_number(equivalent_diameter=equivalent_diameter)

    def reynolds_circular_session(self, diameter):
        return self._reynolds_circular_square(equivalent_diameter=diameter)

    def reynolds_square_session(self, side):
        return self._reynolds_circular_square(equivalent_diameter=side)

    def reynolds_rectangular_session(self, base, height):
        validate = ParamValidator()
        base = validate("Base", base)
        height = validate("Height", height)
        return self._reynolds_number(
            equivalent_diameter=(2 * base * height) / (base + height)
        )


class _FlowTypes(Enum):
    """Enumeration to represent the flow type."""

    LAMINAR: str = "laminar"
    TURBULENT: str = "turbulent"
    MIXED: str = "mixed"


class FluidFlowType:
    def __init__(
        self,
        flow_rate: float,
        viscosity40: float,
        viscosity100: float,
        temperature: float,
    ) -> None:
        self._reynolds_number = ReynoldsNumber(
            flow_rate, viscosity40, viscosity100, temperature,
        )

    @staticmethod
    def _flow_type(number: float) -> str:
        """Determine the flow type of a fluid.

        Re <= 2100 => Laminar flow
        2100.0 < reynolds <= 4000.0 => Mixed flow
        Re > 4000 => Turbulent flow
        """
        if number <= 2_100.0:
            return _FlowTypes.LAMINAR
        if number > 4_000.0:
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
