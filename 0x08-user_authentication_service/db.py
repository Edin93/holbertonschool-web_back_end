#!/usr/bin/env python3
"""
Contains DB class to handle data.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """ DB class. """

    def __init__(self):
        """ DB class initialization """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Set and Return the user session. """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Saves the user to the database and Returns the User object.
        """
        if email and hashed_password:
            user = User(
                email=email,
                hashed_password=hashed_password
            )
            self._session.add(user)
            self._session.commit()
            return user
        return None

    def find_user_by(self, **kwargs: object) -> User:
        """
        Return the first row found in the users table as filtered
        by the passed arguments.
        """
        valid_args = ['email', 'hashed_password', 'session_id', 'reset_token']
        input_keys = kwargs.keys()
        for k in input_keys:
            if k not in valid_args:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user
