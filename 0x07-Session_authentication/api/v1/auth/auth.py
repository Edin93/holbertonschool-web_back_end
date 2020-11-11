#!/usr/bin/env python3
"""
Contains Auth class.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class.
    """

    def __init__(self):
        """ Constructor
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if the path is not in the list of strings excluded_paths.
        """
        if path is None or not excluded_paths:
            return True
        excluded_paths = [path[:-1] if path.endswith('/') else path
                          for path in excluded_paths]
        if path.endswith('/'):
            path = path[:-1]
        for ep in excluded_paths:
            if ep == path:
                return False
            if ep.endswith('*'):
                prefixed_path = ep[:-1]
                if prefixed_path in path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        If request doesn’t contain the header key Authorization, returns None
        Otherwise, return the value of the header request Authorization
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return None. request will be the Flask request object.
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request.
        """
        if request is None:
            return None
        return request.cookies.get('_my_session_id', None)
