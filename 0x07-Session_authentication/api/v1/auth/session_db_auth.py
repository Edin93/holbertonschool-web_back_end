#!/usr/bin/env python3
""" Contains SessionDBAuth class
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


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
        found_user = UserSession.search({'session_id': session_id})

        if not found_user:
            return None

        found_user = found_user[0]
        return found_user.user_id

    def destroy_session(self, request=None):
        """
        Destroys the UserSession based on the Session ID
        from the request cookie.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)

        if session_id is None:
            return False

        user_id = user_id_for_session_id(session_id)
        if user_id is None:
            return False

        user = UserSession.search({
            'user_id': user_id,
            'session_id': session_id
        })
        if not user:
            return False
        user[0].remove()
        return True
