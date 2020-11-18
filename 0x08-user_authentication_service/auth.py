#!/usr/bin/env python3
"""
Contains Authentication methods.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password with bcrypt.hashpw
    """
    pw = password.encode('utf-8')
    hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
    return hashed_pw
