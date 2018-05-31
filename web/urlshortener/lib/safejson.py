"""
    Handles json encoding
"""
from functools import partial
import datetime
from flask import json
import decimal


def default(obj):  # pragma: no cover
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    if isinstance(obj, decimal.Decimal):
        return float(obj)

    return json.JSONEncoder.default(obj, obj)

dumps = partial(json.dumps, default=default)
loads = json.loads
