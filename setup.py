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

"""This module provides the setup.py script."""

from pathlib import Path
from typing import Dict

from setuptools import find_packages
from setuptools import setup

__here__ = Path().cwd()

# Load the package's __init__.py module as a dictionary.
__about__: Dict = {}
with Path(__here__, "lubepy", "__init__.py").open(encoding="UTF-8") as f:
    exec(f.read(), __about__)

# Import the README.md and use it as the long-description.
try:
    with Path(__here__, "README.md").open(encoding="utf-8") as f:
        __long_description__ = "\n" + f.read()
except FileNotFoundError:
    __long_description__ = __about__["DESCRIPTION"]


setup(
    name=__about__["NAME"],
    version=__about__["VERSION"],
    description=__about__["DESCRIPTION"],
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    author=__about__["AUTHOR"],
    author_email=__about__["EMAIL"],
    python_requires=__about__["REQUIRES_PYTHON"],
    url=__about__["URL"],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    license="GNU General Public License, Version 2, June 1991",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords="machinery lubrication, oil, grease, lubrication engineering",
    platforms=["linux", "darwin"],
)
