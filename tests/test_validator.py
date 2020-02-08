#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: test_validator.py
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

"""This module provides tests for validator.py."""


class TestValidator:
    """Class to test Validator class."""

    # @nose.tools.raises(ValueError)
    # def test_float_non_valid_number(self):
    #     self.valid_float = 'n'

    # def test_float_valid_number(self):
    #     self.valid_float = '1,2'
    #     assert self.valid_float == 1.2

    # @nose.tools.raises(ValueError)
    # def test_positive_non_zero(self):
    #     self.positive_non_zero = -15

    # def test_validate_float(self):
    #     assert self.validator.validate_float('Variable', 1.02) == 1.02

    # def test_validate_float_string_float_input(self):
    #     assert self.validator.validate_float('Variable', '1.02') == 1.02

    # def test_validate_float_string_spaced_input(self):
    #     assert self.validator.validate_float('Variable', ' 1.02   ') == 1.02

    # def test_validate_float_string_coma_input(self):
    #     assert self.validator.validate_float('Variable', '1,02') == 1.02

    # @nose.tools.raises(ValueError)
    # def test_validate_float_inf_input(self):
    #     self.validator.validate_float('Variable', 'inf')

    # @nose.tools.raises(ValueError)
    # def test_validate_float_negative_inf_input(self):
    #     self.validator.validate_float('Variable', '-inf')

    # @nose.tools.raises(ValueError)
    # def test_validate_float_empty_string_input(self):
    #     self.validator.validate_float('Variable', '')

    # @nose.tools.raises(ValueError)
    # def test_validate_float_string_input(self):
    #     self.validator.validate_float('Variable', 'string')

    # def test_validate_float_int_input(self):
    #     assert self.validator.validate_float('Variable', 10) == 10.0

    # @nose.tools.raises(ConceptError)
    # def test_validate_lower_limit(self):
    #     self.validator.validate_lower_limit('Variable', 15, 16)

    # def test_validate_lower_limit_none(self):
    #     assert self.validator.validate_lower_limit(15, 14) is None
