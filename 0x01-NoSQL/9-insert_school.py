#!/usr/bin/env python3
"""
inserting a record into a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    this will return a record
    """
    if not kwargs:
        return 
    return mongo_collection.insert_one(kwargs).inserted_id