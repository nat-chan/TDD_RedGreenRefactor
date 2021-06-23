#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# usage: $ oj generate-input 'python3 generate.py'
import random
import argparse

def main(length_max: int, value_max: int):
    length = random.randint(1, length_max)
    values = [random.randint(0, value_max) for _ in range(length)]
    print(length)
    print(*values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--length_max', type=int, default=10, help='max length of output list')
    parser.add_argument('--value_max', type=int, default=999, help='max value of output list')
    args = parser.parse_args()
    main(args.length_max, args.value_max)
