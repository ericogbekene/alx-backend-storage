#!/usr/bin/env python3
"""
module to return the details of a collection in mongodb
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    list all records from this collection
    """
    return mongo_collection.find()