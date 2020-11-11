#!/usr/bin/env python3
"""
Contains SessionExpAuth class.
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
import uuid
from models.user import User
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class.
    """

    def __init__(self):
        """
        Constructor.
        """
        super()
        if not getenv('SESSION_DURATION'):
            self.session_duration = 0
        else:
            try:
                self.session_duration = int(getenv('SESSION_DURATION'), 0)
            except Exception as e:
                self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Create a session ID.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a User ID based on a Session ID.
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        dic = self.user_id_by_session_id.get(session_id, None)
        if self.session_duration <= 0:
            return dic.user_id
        if 'created_at' not in dic.keys():
            return None
        timing = timedelta(seconds=self.session_duration) + dic['created_at']
        if timing < datetime.now():
            return None
        return dic.get('user_id', None)
