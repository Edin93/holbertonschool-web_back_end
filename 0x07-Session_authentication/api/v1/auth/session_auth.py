#!/usr/bin/env python3
"""
Contains SessionAuth class.
"""
from api.v1.auth.auth import Auth
from os import getenv
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    SessionAuth class.
    """

    user_id_by_session_id = {}

    def __init__(self):
        """ Constructor.
        """
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for user_id.
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        sessionId = str(uuid.uuid4())
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID.
        """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        user_id = self.user_id_by_session_id.get(session_id, None)
        return user_id

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value.
        """
        cookie_value = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_value)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout.
        """
        if request is None:
            return False
        sessionId = self.session_cookie(request)
        if not sessionId:
            return False
        userId = self.user_id_for_session_id(sessionId)
        if not userId:
            return False
        del self.user_id_by_session_id[sessionId]
        return True
