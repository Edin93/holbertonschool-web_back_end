#!/usr/bin/env python3
"""
Module contains a function that returns all students sorted by average score.
"""



def top_students(mongo_collection):
    """ Returns all the students sorted by average score. """

    result = mongo_collection.aggregrate([
        {
            "$project": {
                "averageScore": { "$size": "$topics"}
            }
        }
    ])
    return result
