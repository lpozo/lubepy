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

"""This module provides viscosity calculations."""

import math

from lubepy import MAX_VISCOSITY_40, MAX_VISCOSITY_100, MIN_VISCOSITY
from lubepy.validator.core import (
    validate_viscosity,
    validate_viscosity_index,
    validate_temperature,
)


def viscosity_at_40(viscosity100: float, index: float) -> float:
    """Calculate the Kinematic Viscosity (KV) at 40°C.

    Valid for viscosities under 2000 cSt at 40°C.
    """
    _viscosity = _viscosity100 = validate_viscosity(viscosity100, "100")
    _index = validate_viscosity_index(index)
    while (
        _viscosity_index(_viscosity, _viscosity100) >= _index
        and _viscosity <= MAX_VISCOSITY_40
    ):
        _viscosity += 0.05

    return round((_viscosity * 100 + 0.1) / 100, 2)


def viscosity_at_100(viscosity40: float, index: float) -> float:
    """Calculate the Kinematic Viscosity (KV) at 100°C.

    Valid for viscosities between 2 and 500 cSt at 100°C.
    """
    _viscosity = MIN_VISCOSITY
    _viscosity40 = validate_viscosity(viscosity40, "40")
    _index = validate_viscosity_index(index)
    while (
        _viscosity_index(_viscosity40, _viscosity) <= _index
        and _viscosity <= MAX_VISCOSITY_100
    ):
        _viscosity += 0.01

    return round((_viscosity * 100 + 0.01) / 100, 2)


_TO_KELVIN = 273.15


def viscosity_at_any_temp(
    viscosity40: float, viscosity100: float, temperature: float
) -> float:
    """Calculate the kinematic viscosity at any temperature (ASTM D341)."""
    _viscosity40 = validate_viscosity(viscosity40, "40")
    _viscosity100 = validate_viscosity(viscosity100, "100")
    _temperature = validate_temperature(temperature)

    x = math.log10(math.log10(_viscosity40 + 0.7))
    y = math.log10(math.log10(_viscosity100 + 0.7))
    t0 = math.log10(40 + _TO_KELVIN)
    t1 = math.log10(100 + _TO_KELVIN)
    target_t = math.log10(_temperature + _TO_KELVIN)
    b = (x - y) / (t1 - t0)
    a = x + b * t0
    v = 10 ** (10 ** (a - b * target_t)) - 0.7

    return round(v, 2)


def viscosity_index(viscosity40: float, viscosity100: float) -> float:
    """Calculate the Viscosity Index (VI) by ASTM-D2270.

    - Viscosity Index Up to and Including 100

           (L - KV40)
    VI = ------------- * 100
            (L - H)

    where:
        KV40:  kinematic viscosity at 40°C of the oil whose viscosity
                index is to be calculated mm^2/s (cSt).
        L: kinematic viscosity at 40°C of an oil of 0 viscosity
            index having the same kinematic viscosity at 100°C as
            the oil whose viscosity index is to be calculated,
            mm^2/s (cSt)
        H: kinematic viscosity at 40°C of an oil of 100 viscosity
            index having the same kinematic viscosity at 100°C as
            the oil whose viscosity index is to be calculated mm 2 /s
            (cSt)

    L = a * KV100^2 + b * KV100 + c

    where:
        KV100: kinematic viscosity at 100°C of the oil whose viscosity
                index is to be calculated, mm^2/s (cSt)
        a, b, c: interpolation coefficients

    H = d * KV100^2 + e * KV100 + f
    where:
        d, e, f: interpolation coefficients

    - Viscosity Index of 100 and Greater

            (10^N - 1)
    VI = --------------- + 100
             0.00715

    where:
              log10(H) - log10(KV40)
        N = --------------------------
                  log10(KV100)
    """
    return _viscosity_index(viscosity40, viscosity100)


def _viscosity_index(viscosity40: float, viscosity100: float) -> float:
    """Calculate the Viscosity Index (VI) by ASTM-D2270."""
    _viscosity40 = validate_viscosity(viscosity40, "40")
    _viscosity100 = validate_viscosity(viscosity100, "100")
    upper = float("inf")
    interpolation_coefs = {
        (2.0, 3.8): (1.14673, 1.7576, -0.109, 0.84155, 1.5521, -0.077),
        (3.8, 4.4): (3.38095, -15.4952, 33.196, 0.78571, 1.7929, -0.183),
        (4.4, 5.0): (2.5, -7.2143, 13.812, 0.82143, 1.5679, 0.119),
        (5.0, 6.4): (0.101, 16.635, -45.469, 0.04985, 9.1613, -18.557),
        (6.4, 7.0): (3.35714, -23.5643, 78.466, 0.22619, 7.7369, -16.656),
        (7.0, 7.7): (0.01191, 21.475, -72.870, 0.79762, -0.7321, 14.61),
        (7.7, 9.0): (0.41858, 16.1558, -56.040, 0.05794, 10.5156, -28.240),
        (9.0, 12.0): (0.88779, 7.5527, -16.600, 0.26665, 6.7015, -10.810),
        (12.0, 15.0): (0.7672, 10.7972, -38.180, 0.20073, 8.4658, -22.490),
        (15.0, 18.0): (0.97305, 5.3135, -2.200, 0.28889, 5.9741, -4.930),
        (18.0, 22.0): (0.97256, 5.25, -0.980, 0.24504, 7.416, -16.730),
        (22.0, 28.0): (0.91413, 7.4759, -21.820, 0.20323, 9.1267, -34.230),
        (28.0, 40.0): (0.87031, 9.7157, -50.770, 0.18411, 10.1015, -46.750),
        (40.0, 55.0): (0.84703, 12.6752, -133.310, 0.17029, 11.4866, -80.620),
        (55.0, 70.0): (0.85921, 11.1009, -83.19, 0.1713, 11.368, -76.940),
        (70.0, upper): (0.83531, 14.6731, -216.246, 0.16841, 11.8493, -96.947),
    }

    a, b, c, d, e, f = [0.0] * 6

    for k, v in interpolation_coefs.items():
        if k[0] <= _viscosity100 < k[1]:
            a, b, c, d, e, f = v
            break

    L = a * _viscosity100 ** 2 + b * _viscosity100 + c

    H = d * _viscosity100 ** 2 + e * _viscosity100 + f

    if _viscosity40 >= H:
        return round(((L - _viscosity40) / (L - H)) * 100)

    N = (math.log10(H) - math.log10(_viscosity40)) / math.log10(_viscosity100)

    return round(((10 ** N - 1) / 0.00715) + 100)
