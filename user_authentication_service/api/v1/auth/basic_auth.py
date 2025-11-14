#!/usr/bin/env python3
"""
auth module for the API
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth"""

    @staticmethod
    def extract_base64_authorization_header(authorization_header: str) -> str:
        """Extracts the base64 encoded header from the authorization header."""
        if (
            not authorization_header
            or not isinstance(authorization_header, str)
            or not authorization_header.startswith("Basic ")
        ):
            return None
        return authorization_header.split(" ")[1]

    @staticmethod
    def decode_base64_authorization_header(
                                            base64_authorization_header: str
                                            ) -> str:
        """Decodes the base64 encoded header."""
        if not base64_authorization_header or not isinstance(
            base64_authorization_header, str
        ):
            return None
        try:
            base_decode = b64decode(
                base64_authorization_header.encode("utf-8"))
            return base_decode.decode("utf-8")
        except Exception:
            return None

    @staticmethod
    def extract_user_credentials(
        decoded_base64_authorization_header: str,
    ) -> (str, str):
        """Extracts the user credentials (email, password)
        from the decoded header."""
        if (
            not decoded_base64_authorization_header
            or not isinstance(decoded_base64_authorization_header, str)
            or ":" not in decoded_base64_authorization_header
        ):
            return None, None
        return decoded_base64_authorization_header.split(":")

    @staticmethod
    def user_object_from_credentials(
                                    user_email: str, user_pwd: str
                                    ) -> TypeVar("User"):
        """Returns the user object matching the provided
        email and password."""
        if (
            not user_email
            or not isinstance(user_email, str)
            or not user_pwd
            or not isinstance(user_pwd, str)
        ):
            return None
        users = User.search({"email": user_email})
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """current_user"""
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            userPass = self.extract_user_credentials(decodeValue)
            user = self.user_object_from_credentials(userPass[0], userPass[1])
            return user
        except Exception:
            return None
