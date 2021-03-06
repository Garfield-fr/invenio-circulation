# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
# Copyright (C) 2019 RERO.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Circulation API."""

from datetime import timedelta


def patron_exists(patron_pid):
    """Return True if patron exists, False otherwise."""
    return True


def item_exists(item_pid):
    """Return True if item exists, False otherwise."""
    return True


def is_item_available(item_pid):
    """Return if item is available for checkout."""
    return True


def can_be_requested(item_pid=None, document_pid=None):
    """Return if record can be requested."""
    return True


# NOTE: Its on purpose `ref` and not `$ref` so it doesn't try to resolve
def item_ref_builder(item_pid):
    """Return the $ref for item_pid."""
    return {"ref": "{}".format(item_pid)}


def item_location_retriever(item_pid):
    """Retrieve the location pid of the passed item pid."""
    return ""


def get_default_loan_duration(loan):
    """Return a default loan duration in number of days."""
    return 30


def get_default_extension_duration(loan):
    """Return a default extension duration in number of days."""
    return 30


def get_default_extension_max_count(loan):
    """Return a default extensions max count."""
    return float("inf")


def is_loan_duration_valid(loan):
    """Validate the loan duration."""
    return loan["end_date"] > loan["start_date"] and loan["end_date"] - loan[
        "start_date"
    ] < timedelta(days=60)
