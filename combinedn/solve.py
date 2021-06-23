#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from combinedn import CombinedNumber
import argparse

def parse() -> Tuple[int, List[int]]:
    length = int(input())
    values = list(map(int, input().split()))
    assert length == len(values)
    return length, values

def main(solver: Callable[[List[int]], str]):
    length, values = parse()
    ans = solver(values)
    print(ans)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--solver', type=str, default='slow_answer', help='solver function')
    args = parser.parse_args()
    solver = getattr(CombinedNumber, args.solver)
    main(solver)
