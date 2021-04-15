#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群6089740 144081101
# CreateDate: 2020-11-25
def fib(n):
    if n == 0: return n  # special case
    last = 0  # initially set to fib(0)
    next = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next


if __name__ == "__main__":
    print(fib(2))
    print(fib(50))