#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群6089740 144081101
# CreateDate: 2019-12-29

def gcd(q,p):    
# 求最大公约数
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    result = gcd(x, y)
    return gcd(x, y) == 1

if __name__ == '__main__':   
    print(gcd(17, 13))
    print(is_coprime(17, 13))
    print(gcd(17, 21))
    print(is_coprime(17, 21))
    print(gcd(15, 21))
    print(is_coprime(15, 21))
    print(gcd(25, 45))
    print(is_coprime(25, 45))
    print(gcd(15, 45))
    print(is_coprime(15, 45))