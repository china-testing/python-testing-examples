#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：630011153 144081101 
# CreateDate: 2020-7-7 钉钉或微信pythontesting

def mysum(*numbers):
    """
    实现内置函数sum()
    接受任意数量的数字参数作为输入。返回这些数字的总和。
    如果调用时没有任何参数，返回0
    """
    output = 0
    for number in numbers:
        output += number
    return output

if __name__ == '__main__':
    print(mysum(1, 2, 3, 4, 5))