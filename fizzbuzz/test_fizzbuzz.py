#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from fizzbuzz import FizzBuzz
import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_出力はstrである(self):
        self.assertEqual(str, type(FizzBuzz.single_line_answer(1)))

    def test_数値の1を渡したら文字列の1を返す(self):
        self.assertEqual("1", FizzBuzz.single_line_answer(1))

    def test_数値の2を渡したら文字列の2を返す(self):
        self.assertEqual("2", FizzBuzz.single_line_answer(2))

    def test_intの3を渡したら文字列Fizzを返す(self):
        self.assertEqual("Fizz", FizzBuzz.single_line_answer(3))

    def test_intの6を渡したら文字列Fizzを返す(self):
        self.assertEqual("Fizz", FizzBuzz.single_line_answer(6))

    def test_intの5を渡したら文字列Buzzを返す(self):
        self.assertEqual("Buzz", FizzBuzz.single_line_answer(5))

    def test_intの10を渡したら文字列Buzzを返す(self):
        self.assertEqual("Buzz", FizzBuzz.single_line_answer(10))

    def test_intの15を渡したら文字列FizzBuzzを返す(self):
        self.assertEqual("FizzBuzz", FizzBuzz.single_line_answer(15))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
