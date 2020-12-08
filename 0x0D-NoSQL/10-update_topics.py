#!/usr/bin/env python3
"""
Module contains a function that changes all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school documents based on the name.
    """
    if mongo_collection and name:
        mongo_collection.update_many(
            {'name': name},
            {
                '$set': {'topics': topics}
            }
        )
