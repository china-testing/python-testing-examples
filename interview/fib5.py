#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群6089740 144081101
# CreateDate: 2020-11-25
def fib5(n):
    yield 0  # special case
    if n > 0: yield 1  # special case
    last = 0  # initially set to fib(0)
    next = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step


if __name__ == "__main__":
    for i in fib5(50):
        print(i)