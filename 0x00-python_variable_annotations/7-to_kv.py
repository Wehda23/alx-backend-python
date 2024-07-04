#!/usr/bin/env python3
"""
This script is used to generate the data for the paper
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key-value pair to a tuple of (key, value)
    """
    return (k, v**2)
