# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# invenio-dm-tugraz is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Simple test of version import."""

from __future__ import absolute_import, print_function


def test_version():
    """Test version import."""
    from invenio_dm_tugraz import __version__
    assert __version__
