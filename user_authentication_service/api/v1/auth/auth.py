#!/usr/bin/env python3
"""
auth module for the API
"""
import os
from typing import List
import typing

T = typing.TypeVar('T')


class Auth():
    """
    auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the value of the Authorization header"""
        if request is None or not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def session_cookie(self, request=None):
        """Get the value of the session cookie from the request"""
        if request is None:
            return None
        SESSION_NAME = os.environ.get('SESSION_NAME')
        if SESSION_NAME is None:
            return None
        return request.cookies.get(SESSION_NAME)

    def current_user(self, request=None) -> T:
        """current_user"""
        return None
