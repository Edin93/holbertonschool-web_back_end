#!/usr/bin/env python3
"""
Logging module.
"""
import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        '''Returns a log'''
        logging.basicConfig(level=record.levelname, format=self.FORMAT)
        return logging.info(filter_datum(self.fields, self.REDACTION,
                            record.msg, self.SEPARATOR))


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    '''Returns a log message.'''
    return (separator.join(x if x.split('=')[0] not in fields else re.sub(
        r'=.*', '=' + redaction, x) for x in message.split(separator)))
