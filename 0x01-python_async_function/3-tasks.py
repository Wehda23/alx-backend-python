#!/usr/bin/env python3
"""
A basic implmentation of Asynchronous programming in python
"""
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Measures the time it takes to execute n tasks
    """
    return asyncio.create_task(wait_random(max_delay))
