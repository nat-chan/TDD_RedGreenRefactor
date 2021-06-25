#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from itertools import permutations

class MyStr(str):
    def __lt__(self, other):
        return int(self+other) < int(other+self)

class CombinedNumber:
    @classmethod
    def slow_answer(cls, arr: List[int]) -> str:
        """
        実装の方針：順列全探索
        説明：問題の仕様を愚直に実装したもので、遅いが確実な解答が得られる。
        時間計算量: O(N!)
        """
        ans = ''
        for p in permutations(arr):
            tmp = ''.join(map(str, p))
            ans = max(ans, tmp)
        return ans

    @classmethod
    def fast_answer(cls, arr: List[int]) -> str:
        """
        実装の方針：クイックソート
        説明：比較関数を適切に定義し、クイックソートした。
        時間計算量: O(NlogN)
        """
        arr = [MyStr(a) for a in arr]
        arr.sort(reverse=True)
        return ''.join(arr)
