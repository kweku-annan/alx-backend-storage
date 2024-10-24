#!/usr/bin/env python3
"""Creates a Cache class"""
import redis
from typing import Union, Callable, Optional, Any
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

    def get(self, key: str, fn: Callable = None):
        """Takes a key and a Callable and converts data back"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Parametrize get() method with the string type"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Parametrize get() method with the int type"""
        return self.get(key, lambda x: int(x.decode('utf-8')))
