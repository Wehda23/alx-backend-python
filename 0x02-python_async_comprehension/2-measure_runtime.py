#!/usr/bin/env python3
"""
Asynchronous programming in python
"""
from typing import List
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> List[float]:
    """
    Calculates the time for running async comperhension four times
    """
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    start = time.time()
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
