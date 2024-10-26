#!/usr/bin/env python3
"""Lists all collections in a collection"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    all_collections = mongo_collection.find()
    return all_collections