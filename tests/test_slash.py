#!/usr/bin/env python

"""
Test getting "/"
"""

import pytest
from mock import patch, call
from prettypublictest import hello_world


def test_hello_world():
    assert hello_world() == "HI!"
