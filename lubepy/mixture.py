# -*- coding: utf-8 -*-

# File name: mixture.py
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

"""This module provides OilMixture Class."""

from collections import namedtuple
import math


def mixture_viscosity(
    first_viscosity: float,
    first_oil_percent: float,
    second_viscosity: float,
    temperature: str,
) -> float:
    """Return the resulting viscosity of a mix of two base oils."""
    return OilMixture(first_viscosity, second_viscosity,).mixture_viscosity(
        first_oil_percent, temperature
    )


def mixture_proportions(
    first_viscosity: float,
    second_viscosity: float,
    desired_viscosity: float,
    temperature: str,
):
    """Return proportions to get a mixture of a given viscosity."""
    return OilMixture(first_viscosity, second_viscosity,).mixture_proportions(
        desired_viscosity, temperature
    )


class OilMixture:
    """Class to provide calculations on oil mixtures."""

    def __init__(self, first_viscosity: float, second_viscosity: float,) -> None:
        """Class initializer."""
        self.first_viscosity = first_viscosity
        self.second_viscosity = second_viscosity
        self.temp_map = {"100": 1.8, "40": 4.1, "-5": 1.9}

    def mixture_viscosity(self, first_oil_percent: float, temperature: str) -> float:
        """Return the resulting viscosity of a mix of two base oils.

        Mixture KV = e ^ (a * e ^ (x1 * log(b / a))) - K

        Where:
            K: Temperature coefficient
            x1: Percent coefficient for base oil # 1
            a = log(KV2 + K)
            b = log(KV1 + K)
                KV1, KV2: Kinematic Viscosity of oil # 1 and # 2 (cSt)
        """
        K = self.temp_map[temperature]
        x1 = first_oil_percent / 100
        a = math.log(self.second_viscosity + K)
        b = math.log(self.first_viscosity + K)
        mix_viscosity = math.exp(a * math.exp(x1 * math.log(b / a))) - K

        return round(mix_viscosity, 2)

    Proportions = namedtuple("Proportions", ["first_oil_percent", "second_oil_percent"])

    def mixture_proportions(self, desired_viscosity: float, temperature: str):
        """Return proportions to get a mixture of a given viscosity.

        first_oil_percent = 100 * (math.log(a / c) / math.log(b / c))

        Where:
            K: Temperature coefficient
            a = math.log(desired_viscosity + K)
            b = math.log(KV1 + K)
            c = math.log(KV2 + K)
        """

        # if not(self.first_viscosity < desired_viscosity < self.second_viscosity or
        #         self.second_viscosity < desired_viscosity < self.fi):
        #     raise ViscosityIntervalError('Mixture viscosity must be inside '
        #                                  'the viscosity interval')

        K = self.temp_map[temperature]
        a = math.log(desired_viscosity + K)
        b = math.log(self.first_viscosity + K)
        c = math.log(self.second_viscosity + K)
        first_oil_percent = 100 * (math.log(a / c) / math.log(b / c))
        second_oil_percent = 100 - first_oil_percent

        return self.Proportions(round(first_oil_percent, 2), round(second_oil_percent, 2))
