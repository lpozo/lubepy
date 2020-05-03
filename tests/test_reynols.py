#!/usr/bin/env python3
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

"""This module provides tests for reynolds.py."""

import pytest
from pytest import param

from lubepy.reynolds import FlowType, Reynolds, flow_type, reynolds_number


class TestReynolds:
    """Class to test Reynolds."""

    def test_reynolds_number(self):
        reynolds = Reynolds(velocity=15.0, length=0.10, viscosity=3.0)
        assert reynolds.reynolds_number() == 0.5

    def test_reynolds_number_func(self):
        assert reynolds_number(15.0, 0.10, 3) == 0.5

    @pytest.mark.parametrize(
        "velocity, length, viscosity, expected",
        [
            param(15.0, 0.1, 3.0, FlowType.LAMINAR),
            param(600.0, 20.0, 3.0, FlowType.TURBULENT),
            param(600.0, 15.0, 3.0, FlowType.MIXED),
        ],
    )
    def test_reynolds_flow_type(self, velocity, length, viscosity, expected):
        reynolds = Reynolds(velocity, length, viscosity)
        assert reynolds.flow_type() == expected

    def test_reynolds_flow_type_func(self):
        assert flow_type(15.0, 0.10, 3) == FlowType.LAMINAR
