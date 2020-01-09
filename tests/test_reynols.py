#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: tests_reynolds.py
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

"""This module provides tests for reynolds.py."""

from lubepy.reynolds import Reynolds
from lubepy.reynolds import reynolds_number
from lubepy.reynolds import flow_type


class TestReynolds:
    """Class to test Reynolds."""

    def setup_method(self):
        self.reynolds = Reynolds(velocity=15.0, length=0.10, viscosity=3.0)

    def test_reynolds_number(self):
        assert self.reynolds.reynolds_number() == 0.5

    def test_reynolds_number_func(self):
        assert reynolds_number(15.0, 0.10, 3) == 0.5

    def test_reynolds_flow_type(self):
        assert self.reynolds.flow_type() == 'laminar'

    def test_reynolds_flow_type_func(self):
        assert flow_type(15.0, 0.10, 3) == 'laminar'
