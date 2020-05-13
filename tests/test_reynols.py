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
        "velocity, viscosity, diameter, expected",
        [
            param(15.0, 32.0, 0.15, 0.1),
            param(6_000.0, 5.0, 2.0, 2_400.0),
            param(10_000.0, 5.0, 2.5, 5_000.0),
        ],
    )
    def test_reynolds_circular_session(
        self, velocity, viscosity, diameter, expected
    ):
        reynolds = ReynoldsNumber(velocity, viscosity)
        assert reynolds.reynolds_circular_session(diameter) == expected

    @pytest.mark.parametrize(
        "velocity, viscosity, diameter, expected",
        [
            param(15.0, 32.0, 0.15, 0.1),
            param(6_000.0, 5.0, 2.0, 2_400.0),
            param(10_000.0, 5.0, 2.5, 5_000.0),
        ],
    )
    def test_reynolds_circular_session_func(
        self, velocity, viscosity, diameter, expected
    ):
        assert (
            reynolds_circular_session(velocity, viscosity, diameter)
            == expected
        )

    @pytest.mark.parametrize(
        "velocity, viscosity, side, expected",
        [
            param(15.0, 32.0, 0.15, 0.1),
            param(6_000.0, 5.0, 2.0, 2_400.0),
            param(10_000.0, 5.0, 2.5, 5_000.0),
        ],
    )
    def test_reynolds_square_session_func(
        self, velocity, viscosity, side, expected
    ):
        assert reynolds_square_session(velocity, viscosity, side) == expected

    @pytest.mark.parametrize(
        "velocity, viscosity, base, height, expected",
        [
            param(15.0, 32.0, 0.15, 0.2, 0.1),
            param(6_000.0, 5.0, 2.0, 5, 3_428.6),
            param(10_000.0, 5.0, 2.5, 10, 8_000.0),
        ],
    )
    def test_reynolds_rectangular_session_func(
        self, velocity, viscosity, base, height, expected
    ):
        assert (
            reynolds_rectangular_session(velocity, viscosity, base, height)
            == expected
        )

    @pytest.mark.parametrize(
        "velocity, viscosity, diameter, expected",
        [
            param(15.0, 32.0, 0.15, _FlowTypes.LAMINAR),
            param(6_000.0, 5.0, 2.0, _FlowTypes.MIXED),
            param(10_000.0, 5.0, 2.5, _FlowTypes.TURBULENT),
        ],
    )
    def test_flow_type_circular_session(
        self, velocity, viscosity, diameter, expected
    ):
        flow = FluidFlowType(velocity, viscosity)
        assert flow.flow_type_circular_session(diameter) == expected

    @pytest.mark.parametrize(
        "velocity, viscosity, diameter, expected",
        [
            param(15.0, 32.0, 0.15, _FlowTypes.LAMINAR),
            param(6_000.0, 5.0, 2.0, _FlowTypes.MIXED),
            param(10_000.0, 5.0, 2.5, _FlowTypes.TURBULENT),
        ],
    )
    def test_flow_type_circular_session_func(
        self, velocity, viscosity, diameter, expected
    ):
        assert (
            flow_type_circular_session(velocity, viscosity, diameter)
            == expected
        )

    @pytest.mark.parametrize(
        "velocity, viscosity, side, expected",
        [
            param(15.0, 32.0, 0.15, _FlowTypes.LAMINAR),
            param(6_000.0, 5.0, 2.0, _FlowTypes.MIXED),
            param(10_000.0, 5.0, 2.5, _FlowTypes.TURBULENT),
        ],
    )
    def test_flow_type_square_session_func(
        self, velocity, viscosity, side, expected
    ):
        assert flow_type_square_session(velocity, viscosity, side) == expected

    @pytest.mark.parametrize(
        "velocity, viscosity, base, height, expected",
        [
            param(15.0, 32.0, 0.15, 0.2, _FlowTypes.LAMINAR),
            param(6_000.0, 5.0, 2.0, 5, _FlowTypes.MIXED),
            param(10_000.0, 5.0, 2.5, 10, _FlowTypes.TURBULENT),
        ],
    )
    def test_flow_type_rectangular_session_func(
        self, velocity, viscosity, base, height, expected
    ):
        assert (
            flow_type_rectangular_session(velocity, viscosity, base, height)
            == expected
        )
