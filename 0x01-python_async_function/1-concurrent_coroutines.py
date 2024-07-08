#!/usr/bin/env python3
"""
A basic implmentation of Asynchronous programming in python
"""
import asyncio
import random
from typing import List, Optional


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that waits for a random delay between 0 and max_delay seconds
    """
    list_delays: list[Optional[float]] = []
    for _ in range(n):
        list_delays.append(await wait_random(max_delay))
    return list_delays
