#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群6089740 144081101
# CreateDate: 2019-12-29

def fib2(n):
    if n < 2:  # base case
        return n
    return fib2(n - 2) + fib2(n - 1)  # recursive case


if __name__ == "__main__":
    print(fib2(5))
    print(fib2(10))