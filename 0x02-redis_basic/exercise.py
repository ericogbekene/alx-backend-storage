#!/usr/bin/env python3
"""
module to setup a python redis connection
"""


import redis
import uuid
from typing import Union


class Cache:
    """
    class called Cache
    """
    def __init__(self):
        """
        init method
        """
        self._redis = redis.Redis(retry_on_timeout=True)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int]) -> str:
        """
        implementing a store class method
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
