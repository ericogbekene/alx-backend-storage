#!/usr/bin/env python3
"""
module to query a mongodb
"""


def schools_by_topic(mongo_collection, topic):
    """
    lets you search for a specific topic
    """
    return mongo_collection.find({"topic": topic})