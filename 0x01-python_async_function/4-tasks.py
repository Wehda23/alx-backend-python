#!/usr/bin/env python3
"""
A basic implmentation of Asynchronous programming in python
"""
import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


async def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """
    Measures the time it takes to execute n tasks
    """
    return await asyncio.create_task(wait_n(n, max_delay))
