# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
# Copyright (C) 2018 RERO.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Tests for loan item availability."""

import json

import mock


@mock.patch(
    'invenio_circulation.views.is_item_available',
    lambda item_pid: True
)
def test_item_available(app, db, json_headers):
    """Test API GET call to fetch an item availability by PID."""

    with app.test_client() as client:
        res = client.get('/item/1/available', headers=json_headers)
        assert res.status_code == 200
        loan_dict = json.loads(res.data.decode('utf-8'))
        assert loan_dict['available']
