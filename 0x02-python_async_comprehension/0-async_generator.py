#!/usr/bin/env python3
"""
Asynchronous programming in python
"""
import asyncio
import random


async def async_generator():
    """
    Function that Generates random numbers from 0 to 10
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
