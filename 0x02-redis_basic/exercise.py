#!/usr/bin/env python3
"""
module to setup a python redis connection
"""


import redis
import uuid
from typing import Union, Optional


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

    def get(self, key: str, fn: Optional[callable]):
        """
        method to return utf exuivalent option from cache
        """
        if key:
            value = self._redis.get(key)
            if fn:
                return fn(value)

    def get_str(self, key:bytes) -> str:
        """
        to return a str
        """
        return self.get(key, lambda x: x.decode("utf-8"))
    
    def get_int(self, key:bytes) -> int:
        """
        this will return and int from bytes
        """
        return self.get(key, lambda x: int.from_bytes(x, "big"))