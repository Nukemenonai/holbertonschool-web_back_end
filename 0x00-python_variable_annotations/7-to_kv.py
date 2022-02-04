#!/usr/bin/env python3
"""annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple with key and value squared"""
    return (k, v ** 2)
