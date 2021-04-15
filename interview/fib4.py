#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群6089740 144081101
# CreateDate: 2020-11-25
from functools import lru_cache


@lru_cache(maxsize=None)
def fib4(n):
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursive case


if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))