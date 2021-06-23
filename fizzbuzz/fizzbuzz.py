#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *


class FizzBuzz:
    @classmethod
    def single_line_answer(cls, n: int) -> str:
        n_is_multiple_of_3 = n % 3 == 0
        n_is_multiple_of_5 = n % 5 == 0
        if n_is_multiple_of_3 and not n_is_multiple_of_5:
            return 'Fizz'
        if not n_is_multiple_of_3 and n_is_multiple_of_5:
            return 'Buzz'
        if n_is_multiple_of_3 and n_is_multiple_of_5:
            return 'FizzBuzz'
        return str(n)

    @classmethod
    def multiple_line_answer(cls) -> List[str]:
        return [cls.single_line_answer(n) for n in range(1, 100 + 1)]

    @classmethod
    def print_answer(cls) -> None:
        print('\n'.join(cls.multiple_line_answer()))
