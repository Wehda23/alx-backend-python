#!/usr/bin/env python3
"""
Module that returns a function multipler
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier
    Args:
    multiplier (float): The multiplier
    Returns:
    Callable[[float], float]: The function that multiplies a float by multiplier
    """

    def multiplier_func(num: float) -> float:
        """Returns the product of num and multiplier
        Args:
        num (float): The number to multiply
        Returns:
        float: The product of num and multiplier
        """
        return num * multiplier

    return multiplier_func
