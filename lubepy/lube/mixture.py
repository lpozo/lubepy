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

"""This module provides the OilMixture class."""

import math
from collections import namedtuple

from lubepy.exceptions import ConceptError
from lubepy.validator.core import Temperature, validate_viscosity


def mixture_viscosity(
    first_viscosity: float,
    first_oil_percent: float,
    second_viscosity: float,
    temperature: str,
) -> float:
    """Return the resulting viscosity of a mix of two base oils."""
    return OilMixture(
        first_viscosity, second_viscosity, temperature
    ).mixture_viscosity(first_oil_percent)


_Proportions = namedtuple(
    "_Proportions", ["first_oil_percent", "second_oil_percent"]
)


def mixture_proportions(
    first_viscosity: float,
    second_viscosity: float,
    desired_viscosity: float,
    temperature: str,
) -> _Proportions:
    """Return proportions to get a mixture of a given viscosity."""
    return OilMixture(
        first_viscosity, second_viscosity, temperature
    ).mixture_proportions(desired_viscosity)


class OilMixture:
    """Class to provide calculations on oil mixtures."""

    temperature = Temperature("Temperature")

    def __init__(
        self, first_viscosity: float, second_viscosity: float, temperature: str
    ) -> None:
        """Class initializer."""
        self.temperature = temperature
        self.first_viscosity = validate_viscosity(
            first_viscosity, self.temperature
        )
        self.second_viscosity = validate_viscosity(
            second_viscosity, self.temperature
        )
        self.temp_map = {"100": 1.8, "40": 4.1, "-5": 1.9}

    def mixture_viscosity(self, first_oil_percent: float) -> float:
        """Return the resulting viscosity of a mix of two base oils.

        Mixture KV = e ^ (a * e ^ (x1 * log(b / a))) - K

        Where:
            x1: Proportion of base oil # 1
            a = log(KV2 + K)
            b = log(KV1 + K)
                KV1, KV2: Kinematic Viscosity of oil # 1 and # 2 (cSt)
            K: Temperature correction

        """
        K = self.temp_map[self.temperature]
        x1 = first_oil_percent / 100
        a = math.log(self.second_viscosity + K)
        b = math.log(self.first_viscosity + K)
        mix_viscosity = math.exp(a * math.exp(x1 * math.log(b / a))) - K

        return round(mix_viscosity, 2)

    def mixture_proportions(self, desired_viscosity: float) -> _Proportions:
        """Return proportions to get a mixture of a given viscosity.

        first_oil_percent = 100 * (math.log(a / c) / math.log(b / c))

        Where:
            a = math.log(desired_viscosity + K)
            b = math.log(KV1 + K)
            c = math.log(KV2 + K)
                K: Temperature correction

        """

        desired_viscosity = validate_viscosity(
            desired_viscosity, self.temperature
        )

        if not (
            self.first_viscosity <= desired_viscosity <= self.second_viscosity
            or self.second_viscosity
            <= desired_viscosity
            <= self.first_viscosity
        ):
            raise ConceptError(
                "Mixture viscosity must be inside the viscosity interval"
            )

        K = self.temp_map[self.temperature]
        a = math.log(desired_viscosity + K)
        b = math.log(self.first_viscosity + K)
        c = math.log(self.second_viscosity + K)
        first_oil_percent = 100 * (math.log(a / c) / math.log(b / c))
        second_oil_percent = 100 - first_oil_percent

        return _Proportions(
            round(first_oil_percent, 2), round(second_oil_percent, 2)
        )
