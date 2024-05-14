#!/usr/bin/env python3
"""
 Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    look-up for definition
    """
    result = []
    for document in mongo_collection.find():
        result.append(document)
    return result
