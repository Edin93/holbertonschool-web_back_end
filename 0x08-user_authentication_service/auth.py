#!/usr/bin/env python3
"""
Contains Authentication methods.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """
    Hashes a password with bcrypt.hashpw
    """
    pw = password.encode('utf-8')
    hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
    return hashed_pw


def _generate_uuid() -> str:
    """
    Returns a string representation of a new UUID.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Auth class initialization. """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user with the email and password credentials if
        it does not exist and retur its User object.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_pw = _hash_password(password)
            added_user = self._db.add_user(email, hashed_pw)
            return added_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks if email and password are valid user credentials.
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Returns the session ID of the given email.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """
        Returns the user the corresponds to the given session_id
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """
        Updates the corresponding user's session ID to None.
        """
        if user_id is None:
            return None
        try:
            user = self._db.update_user(user_id, session_id=None)
            return user
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Resets user password token.
        """
        try:
            user = self._db.find_user_by(email=email)
            new_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=new_token)
            return new_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Updates the user's password.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hpw = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hpw)
            self._db.update_user(user.id, reset_token=None)
        except NoResultFound:
            raise ValueError
