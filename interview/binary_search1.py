#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论Q群144081101 书籍Q群6089740
# CreateDate: 2019-12-29


def bin_search(items, item):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = items[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    l = list(range(1,30,3)) # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    print(bin_search(l, 7)) # return 2
    print(bin_search(l, 1)) # return 0 
    print(bin_search(l, 29)) # return None