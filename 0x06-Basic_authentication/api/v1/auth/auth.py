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
        Returns False - path
        """
        if path is None or not excluded_paths:
            return True
        excluded_paths = [path[:-1] if path.endswith('/') else path
                          for path in excluded_paths]
        if path.endswith('/'):
            path = path[:-1]
        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None. request will be the Flask request object.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return None. request will be the Flask request object.
        """
        return None
