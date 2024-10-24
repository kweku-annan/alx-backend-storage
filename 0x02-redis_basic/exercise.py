#!/usr/bin/env python3
"""Creates a Cache class"""
import redis
from typing import Union
import uuid


class Cache:
    """Stores an instance of the Redis client as Private"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key, stores the input data in Redis"""
        rand_key = str(uuid.uuid4())
        key = self._redis.set(rand_key, data)
        return rand_key
