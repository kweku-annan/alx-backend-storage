#!/usr/bin/env python3
"""Changes all topics of a school document based on name"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school based on the name"""
    mongo_collection.update_one({name: name}, {"$set": {name: topics}})
