#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from combinedn import CombinedNumber
import unittest


class TestHiker(unittest.TestCase):
    def test_リスト_1_が与えられた時には文字列1を返す(self):
        self.assertEqual("1", CombinedNumber.slow_answer([1]))

    def test_リスト_1_0_が与えられた時には文字列10を返す(self):
        self.assertEqual("10", CombinedNumber.slow_answer([1, 0]))

    def test_リスト_0_1_が与えられた時には文字列10を返す(self):
        self.assertEqual("10", CombinedNumber.slow_answer([0, 1]))

    def test_リスト_9_10_が与えられた時には文字列910を返す(self):
        self.assertEqual("910", CombinedNumber.slow_answer([9, 10]))

    def test_入力引数の配列が破壊されない(self):
        samplecase = [0, 1]
        CombinedNumber.slow_answer(samplecase)
        self.assertEqual([0, 1], samplecase)

    def test_リスト_5_50_56_が与えられた時には文字列56550を返す(self):
        self.assertEqual("56550", CombinedNumber.slow_answer([5, 50, 56]))

    def test_リスト_50_2_1_9_が与えられたときには文字列95021を返す(self):
        self.assertEqual("95021", CombinedNumber.slow_answer([50, 2, 1, 9]))

    def test_リスト_420_42_423_が与えられたときには文字列42423420を返す(self):
        self.assertEqual("42423420", CombinedNumber.slow_answer([420, 42,
                                                                 423]))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
