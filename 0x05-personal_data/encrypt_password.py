#!/usr/bin/env python3
"""
Password hashing.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password."""
    # pw = bytes(password, 'utf-8')
    pw = password.encode('utf-8')
    return bcrypt.hashpw(pw, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if the provided password matches the hashed password."""
    # pw = bytes(password, 'utf-8')
    return bcrypt.checkpw(hashed_password, password.encode('utf-8'))