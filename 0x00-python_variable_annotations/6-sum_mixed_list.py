#!/usr/bin/env python3
"""
Module contains function to sum list values
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function to sum list values
    Args:
    mxd_lst (List[Union[int, float]]): List of mixed values
    Returns:
    float: Sum of list values
    """
    return sum(mxd_lst)
