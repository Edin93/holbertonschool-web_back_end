#!/usr/bin/env python3
"""
Contains SessionAuth class.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class.
    """

    user_id_by_session_id = {}

    def __init__(self):
        """
        Constructor.
        """
        pass

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
