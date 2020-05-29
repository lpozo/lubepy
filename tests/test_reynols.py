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

from lubepy.fluid.reynolds import (
    _FlowTypes,
    FluidFlowType,
    ReynoldsNumber,
    reynolds_circular_session,
    flow_type_circular_session,
    flow_type_square_session,
    flow_type_rectangular_session,
    reynolds_square_session,
    reynolds_rectangular_session,
)


class TestReynolds:
    """Class to test Reynolds."""

    @pytest.mark.parametrize(
        "flow_rate, viscosity40, viscosity100, temperature, diameter, expected",
        [
            param(1_800.0, 320, 24.0, 40, 20.0, 99.6),
            param(600.0, 10, 2.5, 40, 10.0, 2123.8),
            param(600.0, 5, 2.1, 40, 10.0, 4247.5),
        ],
    )
    def test_reynolds_circular_session(
        self,
        flow_rate,
        viscosity40,
        viscosity100,
        temperature,
        diameter,
        expected,
    ):
        reynolds = ReynoldsNumber(
            flow_rate, viscosity40, viscosity100, temperature
        )
        assert reynolds.reynolds_circular_session(diameter) == expected

    @pytest.mark.parametrize(
        "flow_rate, viscosity40, viscosity100, temperature, diameter, expected",
        [
            param(1_800.0, 320, 24.0, 40, 20.0, 99.6),
            param(600.0, 10, 2.5, 40, 10.0, 2123.8),
            param(600.0, 5, 2.1, 40, 10.0, 4247.5),
        ],
    )
    def test_reynolds_circular_session_func(
        self,
        flow_rate,
        viscosity40,
        viscosity100,
        temperature,
        diameter,
        expected,
    ):
        assert (
            reynolds_circular_session(
                flow_rate, viscosity40, viscosity100, temperature, diameter
            )
            == expected
        )

    @pytest.mark.parametrize(
        "flow_rate, viscosity40, viscosity100, temperature, side, expected",
        [
            param(1_800.0, 320, 24.0, 40, 20.0, 99.6),
            param(600.0, 10, 2.5, 40, 10.0, 2123.8),
            param(600.0, 5, 2.1, 40, 10.0, 4247.5),
        ],
    )
    def test_reynolds_square_session_func(
        self, flow_rate, viscosity40, viscosity100, temperature, side, expected
    ):
        assert (
            reynolds_square_session(
                flow_rate, viscosity40, viscosity100, temperature, side
            )
            == expected
        )

    @pytest.mark.parametrize(
        "flow_rate, viscosity40, viscosity100, temperature, base, height, expected",
        [
            param(1_800.0, 320, 24.0, 40, 20.0, 20.0, 99.6),
            param(600.0, 10, 2.5, 40, 10.0, 10.0, 2123.8),
            param(600.0, 5, 2.1, 40, 10.0, 10.0, 4247.5),
        ],
    )
    def test_reynolds_rectangular_session_func(
        self,
        flow_rate,
        viscosity40,
        viscosity100,
        temperature,
        base,
        height,
        expected,
    ):
        assert (
            reynolds_rectangular_session(
                flow_rate, viscosity40, viscosity100, temperature, base, height
            )
            == expected
        )

    @pytest.mark.parametrize(
        "flow_rate, viscosity40, viscosity100, temperature, diameter, expected",
        [
            param(1_800.0, 320, 24.0, 40, 20.0, _FlowTypes.LAMINAR),
            param(600.0, 10, 2.5, 40, 10.0, _FlowTypes.MIXED),
            param(600.0, 5, 2.1, 40, 10.0, _FlowTypes.TURBULENT),
        ],
    )
    def test_flow_type_circular_session_func(
        self,
        flow_rate,
        viscosity40,
        viscosity100,
        temperature,
        diameter,
        expected,
    ):
        assert (
            flow_type_circular_session(
                flow_rate, viscosity40, viscosity100, temperature, diameter
            )
            == expected
        )

    @pytest.mark.parametrize(
        "flow_rate, viscosity40, viscosity100, temperature, side, expected",
        [
            param(1_800.0, 320, 24.0, 40, 20.0, _FlowTypes.LAMINAR),
            param(600.0, 10, 2.5, 40, 10.0, _FlowTypes.MIXED),
            param(600.0, 5, 2.1, 40, 10.0, _FlowTypes.TURBULENT),
        ],
    )
    def test_flow_type_square_session_func(
        self, flow_rate, viscosity40, viscosity100, temperature, side, expected
    ):
        assert (
            flow_type_square_session(
                flow_rate, viscosity40, viscosity100, temperature, side
            )
            == expected
        )

    @pytest.mark.parametrize(
        "flow_rate, viscosity40, viscosity100, temperature, base, height, expected",
        [
            param(1_800.0, 320, 24.0, 40, 20.0, 20.0, _FlowTypes.LAMINAR),
            param(600.0, 10, 2.5, 40, 10.0, 10.0, _FlowTypes.MIXED),
            param(600.0, 5, 2.1, 40, 10.0, 10.0, _FlowTypes.TURBULENT),
        ],
    )
    def test_flow_type_rectangular_session_func(
        self,
        flow_rate,
        viscosity40,
        viscosity100,
        temperature,
        base,
        height,
        expected,
    ):
        assert (
            flow_type_rectangular_session(
                flow_rate, viscosity40, viscosity100, temperature, base, height
            )
            == expected
        )
