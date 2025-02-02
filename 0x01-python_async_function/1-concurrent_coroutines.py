#!/usr/bin/env python3
"""
A basic implmentation of Asynchronous programming in python
"""
from typing import List, Optional
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that waits for a random delay between 0 and max_delay seconds
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    list_delays: list[Optional[float]] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        list_delays.append(delay)
    return list_delays
