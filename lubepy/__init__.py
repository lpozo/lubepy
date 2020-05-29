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

"""This module provides the lubepy package."""

# Package meta-data.
NAME = "lubepy"
DESCRIPTION = (
    "Lubepy provides a basic set of machinery lubrication calculations."
)
URL = "https://github.com/lpozo/lubepy"
EMAIL = "lpozor78@gmail.com"
AUTHOR = "Leodanis Pozo Ramos"
REQUIRES_PYTHON = ">=3.6"
VERSION = "1.0a0"

# Package constants
MIN_VISCOSITY = 2.0  # cSt
MAX_VISCOSITY_MINUS_5 = 10_000.00  # cSt
MAX_VISCOSITY_40 = 2_000.0  # cSt
MAX_VISCOSITY_100 = 500.0  # cSt
MIN_VISCOSITY_INDEX = -25.0  # No unit
MAX_VISCOSITY_INDEX = 400.0  # No unit
MIN_TEMPERATURE = -50.0  # ºC
MAX_TEMPERATURE = 1_200.0  # ºC
MIN_BEARING_DIAMETER = 1.0  # mm
MAX_BEARING_DIAMETER = 100_000.0  # mm
MIN_BEARING_WIDTH = 1.0  # mm
MAX_BEARING_WIDTH = 10_000.0  # mm
MIN_PIPE_EQUIVALENT_DIAMETER = 1.0  # mm
MAX_PIPE_EQUIVALENT_DIAMETER = 1_000.0  # mm
MIN_RPM = 1.0  # 1/s
MAX_RPM = 300_000.0  # 1/s
MIN_ADDITIVE_PERCENT = 0.0  # %
MAX_ADDITIVE_PERCENT = 50.0  # %
MIN_OIL_DENSITY = 0.7  # g/mL
MAX_OIL_DENSITY = 1.5  # g/mL
MIN_FLOW_RATE = 0.1  # L/h
MAX_FLOW_RATE = 5_000.0  # L/h
ASH_CONTRIBUTION = {
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
