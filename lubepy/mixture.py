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


class OilMixture:
    """Class to provide calculations on oil mixtures."""

    def __init__(self,
                 first_viscosity: float,
                 second_viscosity: float,
                 first_oil_percent: float):
        """Class initializer."""
        self.first_viscosity = first_viscosity
        self.second_viscosity = second_viscosity
        self.first_oil_percent = first_oil_percent
        self.temp_map = {'100': 1.8,
                         '40': 4.1,
                         '-5': 1.9}

    def mixture_viscosity(self, temperature: str) -> float:
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
        x1 = self.first_oil_percent / 100
        a = math.log(self.second_viscosity + K)
        b = math.log(self.first_viscosity + K)
        mix_viscosity = math.exp(a * math.exp(x1 * math.log(b / a))) - K

        return round(mix_viscosity, 2)

    # def mix_proportions(self, viscosity0, viscosity1,
    #                     mix_viscosity, temperature):
    #     """Return proportions to get a mixture of a given viscosity."""
    #     # Validate Data
    #     self.viscosity0 = viscosity0
    #     self.viscosity1 = viscosity1
    #     self.mix_viscosity = mix_viscosity

    #     if not(self._viscosity0 < self._mix_viscosity < self._viscosity1 or
    #             self._viscosity1 < self._mix_viscosity < self._viscosity0):
    #         raise ViscosityIntervalError('Mixture viscosity must be inside '
    #                                      'the viscosity interval')

    #     K = self.temp_map[temperature]
    #     a = math.log(self.mix_viscosity + K)
    #     b = math.log(self._viscosity0 + K)
    #     c = math.log(self._viscosity1 + K)
    #     oil1_percent = 10000 * (math.log(a / c) / math.log(b / c)) / 100
    #     oil2_percent = 100 - oil1_percent
    #     Proportions = namedtuple('Proportions', ['oil1', 'oil2'])
    #     return Proportions(round(oil1_percent, 2), round(oil2_percent, 2))
