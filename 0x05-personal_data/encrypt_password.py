#!/usr/bin/env python3
"""
Password hashing.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password."""
    pw = bytes(password, 'utf-8')
    return bcrypt.hashpw(pw, bcrypt.gensalt())
