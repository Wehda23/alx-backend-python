#!/usr/bin/env python3
"""
Asynchronous programming in python
"""
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Returns 10 random numbers
    """
    return [number async for number in async_generator()]
