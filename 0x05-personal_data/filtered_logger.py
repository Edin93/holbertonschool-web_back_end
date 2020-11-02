#!/usr/bin/env python3
"""
Logging module.
"""
import re
from typing import List


def filter_datum(fields: List, redaction: str, msg: str, sep: str) -> str:
    '''Returns a log msg.'''
    return (';'.join(x if x.split('=')[0] not in fields
            else re.sub(r'=.*', '=' + redaction, x) for x in msg.split(sep)))
