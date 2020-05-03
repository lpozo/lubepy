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
    "Lubepy provides basic set of machinery lubrication calculations."
)
URL = "https://github.com/lpozo/lubepy"
EMAIL = "lpozor78@gmail.com"
AUTHOR = "Leodanis Pozo Ramos"
REQUIRES_PYTHON = ">3"
VERSION = (0, 1, 0)
__version__ = ".".join(map(str, VERSION))

# Package constants
LOW_VISCOSITY = 2.0
HIGH_VISCOSITY_40 = 2000.0
HIGH_VISCOSITY_100 = 500.0
TO_KELVIN = 273.15
LOW_INDEX = 1.0
HIGH_INDEX = 400.0
LOW_TEMPERATURE = -50.0
HIGH_TEMPERATURE = 1200.0
