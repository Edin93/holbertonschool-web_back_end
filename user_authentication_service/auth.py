#!/usr/bin/env python3
""" Define Auth class
"""
import bcrypt
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import uuid
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """
    Generate a salted hash of the input password using bcrypt

    Args:
    password (str): The password to hash

    Returns (byte): The hashed password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)

    return hashed.decode('utf-8')


def _generate_uuid() -> str:
    """
    Generate a string representation of a new UUID

    Returns (str): A new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a user in the database.

        Args:
        email (str): The email of the user to register
        password (str): The password of the user to register

        Returns: The User object of the registered
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists.')
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)

            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate login credentials

        Args:
        email (str): The email of user
        password (str): The password provided

        Returns:
        True if the password matches the stored hashed password for the email
        False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(password.encode('utf-8'),
                              user.hashed_password.encode('utf-8'))

    def create_session(self, email: str) -> str:
        """
        Generate user's session_id and store it in DB

        Args:
        email (str): The email of user

        Returns (str):
        generated session_id for the user, or if the user was not found, None
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Fetch login user's data from session_id

        Args:
        session_id (str): user's session_id

        Returns:
        The corresponding User object with session_id
        If the session ID is None or no user is found, None
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except (NoResultFound, InvalidRequestError):
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Delete corresponding user's session_id

        Args:
        user_id (int): user's id

        Returns:
        None
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a reset token and store it in DB

        Args:
        email (str): user's email

        Returns (str):
        token is generated
        """
        try:
            user = self._db.find_user_by(email=email)
        except (NoResultFound, InvalidRequestError):
            raise ValueError

        uuid = _generate_uuid()

        self._db.update_user(user.id, reset_token=uuid)
        return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update user's password

        Args:
        reset_token (str): user's reset token
        password (str): new password for update user's password

        Returns:
        None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except (NoResultFound, InvalidRequestError):
            raise ValueError

        user_hashed_password = _hash_password(password)

        self._db.update_user(
                user.id,
                hashed_password=user_hashed_password,
                reset_token=None
                )
