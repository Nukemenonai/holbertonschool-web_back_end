#!/usr/bin/env python3
"""annotations"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a list of mixed int and float"""
    return sum(mxd_lst)
