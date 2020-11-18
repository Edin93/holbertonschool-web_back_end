#!/usr/bin/env python3
"""
Contains User SQLAlchemy model.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR


Base = declarative_base()


class User(Base):
    """ User class. """
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    email = Column(VARCHAR(250), nullable = False)
    hashed_password = Column(VARCHAR(250), nullable = False)
    session_id = Column(VARCHAR(250), nullable = True)
    reset_token = Column(VARCHAR(250), nullable = True)
