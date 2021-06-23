#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from itertools import permutations


class CombinedNumber:
    @classmethod
    def slow_answer(cls, arr: List[int]) -> str:
        ans = ''
        for p in permutations(arr):
            tmp = ''.join(map(str, p))
            ans = max(ans, tmp)
        return ans
