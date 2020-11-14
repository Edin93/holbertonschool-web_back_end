#!/usr/bin/env python3
""" Contains SessionDBAuth class
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class
    """

    def create_session(self, user_id=None):
        """
        Creates a session ID.
        """
        if user_id is None:
            return None

        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        user_session_data = {
            'session_id': session_id,
            'user_id': user_id
        }
        user_session = UserSession(**user_session_data)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a User ID based on a Session ID.
        """
        if session_id is None:
            return None

        UserSession.load_from_file()
        user = UserSession.search({'session_id': session_id})
        if not user:
            return None

        user = user[0]
        timing = timedelta(seconds=self.session_duration) + user.created_at
        if timing < datetime.now():
            return None
        return user.user_id

    def destroy_session(self, request=None):
        """
        Destroys the UserSession based on the Session ID
        from the request cookie.
        """
        if not request:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_id = user_id_for_session_id(session_id)
        if not user_id:
            return False

        user = UserSession.search({
            'session_id': session_id
        })
        if not user:
            return False
        user[0].remove()
        return True
