#!/usr/bin/env python3
"""
Logging module.
"""
import logging
import mysql.connector
import os
import re
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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
        msg = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            msg, self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    '''Returns a log message.'''
    return (separator.join(x if x.split('=')[0] not in fields else re.sub(
        r'=.*', '=' + redaction, x) for x in message.split(separator)))


def get_logger() -> logging.Logger:
    """Returns a Logger object."""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(RedactingFormatter(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to my_db database."""
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", 'root')
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", '')
    host = os.getenv("PERSONAL_DATA_DB_HOST", 'localhost')
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    cnx = mysql.connector.connect(
        host=host,
        database=db_name,
        user=user,
        password=password
    )

    return cnx


if __name__ == "__main__":
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()

    for row in records:
        msg = ''
        for i in range(5):
            msg += PII_FIELDS[i] + '=' + row[i] + ';'
        msg += 'ip={};last_login={};user_agent={};'.format(
                row[5], row[6], row[7])
        # print(msg)
        # print(RedactingFormatter(PII_FIELDS))
        record = logging.LogRecord('user_data', logging.INFO, None, None,
                                   msg, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        print(formatter.format(record))

    cursor.close()
    db.close()
