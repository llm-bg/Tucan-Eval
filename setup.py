#!/usr/bin/env python3
"""Backward-compatibility shim.

All packaging metadata lives in pyproject.toml (PEP 621). This file only
exists so that very old tooling that does not understand pyproject.toml-only
projects still works with `python setup.py ...`.
"""

from setuptools import setup

setup()
