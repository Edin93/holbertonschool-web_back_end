#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Returns a User object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        # ゲッターメソッドを呼ぶ（遅延初期化）
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Searches for the first user in the database
        that matches the provided key and value
        """
        try:
            found_user = self._session.query(User).filter_by(**kwargs).first()
            if not found_user:
                raise NoResultFound
        except InvalidRequestError:
            raise
        return found_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update the user’s attributes based on the provided keyword arguments.

        Args:
        user_id (int): ID of the user to update
        **kwargs: Arbitrary keyword arguments to update attributes

        Returns: None
        """
        user_attributes = [
                'id',
                'email',
                'hashed_password',
                'session_id',
                'reset_token'
                ]
        user = self.find_user_by(id=user_id)

        for k, v in kwargs.items():
            if k not in user_attributes:
                raise ValueError
            setattr(user, k, v)

        self._session.commit()
        return None
