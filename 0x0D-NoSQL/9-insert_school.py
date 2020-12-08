#!/usr/bin/ehv python3
"""
Module contains a function that inserts a new document in a
collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document based on kwargs and return its _id.
    """
    _id = None
    if mongo_collection and kwargs:
        _id = mongo_collection.insert_one(kwargs).inserted_id
    return _id
