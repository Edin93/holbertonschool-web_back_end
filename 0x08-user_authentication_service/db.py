#!/usr/bin/env python3
"""
Contains the DB class.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:
    """ DB class. """

    def __init__(self):
        """ DB class initialization """
        self._engine = create_engine("sqlite:///a.db", echo=True)
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

    def add_user(self, email, hashed_password):
        """
        Saves the user to the database and Returns the User object.
        """
        if email and hashed_password:
            user = User()
            user.email = email
            user.hashed_password = hashed_password
            return user
        return None
