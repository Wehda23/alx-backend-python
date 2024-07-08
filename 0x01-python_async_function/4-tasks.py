#!/usr/bin/env python3
"""
A basic implmentation of Asynchronous programming in python
"""
import asyncio
from typing import List, Optional


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Measures the time it takes to execute n tasks
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    list_delays: list[Optional[float]] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        list_delays.append(delay)
    return list_delays
