#!/usr/bin/env python3
"""
update a record
"""

if __name__ == "__main__":
    def update_topics(mongo_collection, name, topics):
        """
        function to update a record
        """
        mongo_collection.updateMany({name: name}, {"$set": {topics: topics}})
