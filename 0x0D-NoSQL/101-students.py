#!/usr/bin/env python3
"""
Module contains a function that returns all students sorted by average score.
"""



def top_students(mongo_collection):
    """ Returns all the students sorted by average score. """

    students = []

    for document in mongo_collection.find():

        topics = document.get('topics')
        sum_score = 0

        for topic in topics:
            sum_score += topic.get('score', 0)

        averageScore = sum_score / len(topics)

        student = {
            'name': document.get('name'),
            '_id': document.get('_id'),
            'averageScore': averageScore
        }

        limit = len(students)
        if limit == 0:
            students.append(student)
        else:
            i = 0
            while i < limit and students[i]['averageScore'] > student['averageScore']:
                i += 1
            students.insert(i, student)

    return students
