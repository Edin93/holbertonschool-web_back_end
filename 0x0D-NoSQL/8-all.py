#!/usr/bin/env python3
"""
Module contains a python function that lists all documents in a mongodb collection.
"""


def list_all(mongo_collection):
    """
        Returns all the documents in a given mongo_collection.
    """

    docs = mongo_collection.find()
    if docs:
        return docs
    return []
