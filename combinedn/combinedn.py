#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from itertools import permutations
from functools import total_ordering

@total_ordering
class MyStr(str):
    def __lt__(self, other):
        return int(self+other) < int(other+self)

class CombinedNumber:
    @classmethod
    def slow_answer(cls, arr: List[int]) -> str:
        ans = ''
        for p in permutations(arr):
            tmp = ''.join(map(str, p))
            ans = max(ans, tmp)
        return ans

    @classmethod
    def fast_answer(cls, arr: List[int]) -> str:
        arr = [MyStr(a) for a in arr]
        arr.sort(reverse=True)
        return ''.join(arr)
