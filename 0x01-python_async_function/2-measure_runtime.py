#!/usr/bin/env python3
"""
A basic implmentation of Asynchronous programming in python
"""
import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the time it takes to execute n tasks
    """
    tasks = asyncio.run(wait_n(n, max_delay))
    return sum(tasks) / n
