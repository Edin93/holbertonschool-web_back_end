#!/usr/bin/env python3
"""
Module contains a function that returns the list of the school having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.
    """
    return mongo_collection.find({ "topics": topic })
