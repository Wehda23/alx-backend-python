#!/usr/bin/env python3
"""
This script is used to generate the data for the paper
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of a list if it exists, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
