#!/usr/bin/env python3
"""
Module contains function that sums up float values from list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function sums up float values from list

    Args:
        input_list (List[float]): list of float values

    Returns:
        float: sum of float values
    """
    return sum(input_list)
