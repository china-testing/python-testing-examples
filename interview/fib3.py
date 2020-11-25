#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群630011153 144081101
# CreateDate: 2020-11-25
memo = {0: 0, 1: 1} 

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) 
    return memo[n]


if __name__ == "__main__":
    print(fib3(5))
    print(fib3(50))
