#!/usr/bin/env python3
"""
This script is used to generate the data for the paper
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")


def safely_get_value(
    dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Safely get a value from a dictionary. If the key is not present, return the
    default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
