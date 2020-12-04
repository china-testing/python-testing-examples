#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论Q群144081101 书籍Q群6089740
# CreateDate: 2019-12-29

def bin_search(l,item,high,low=0):
    
    if low > high:
        return None
    
    mid = (low + high) // 2
    value = l[mid]
    if value == item:
        return mid
    elif value > item:
        return bin_search(l, item, mid-1,low)
    else:
        return bin_search(l, item, high, mid+1)

if __name__ == '__main__':
    l = list(range(1,30,3)) # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    print(l)
    n = len(l) - 1
    print(bin_search(l,1,n))  # return 0
    print(bin_search(l,30,n)) # return None
    print(bin_search(l,23,n)) # return None
    print(bin_search(l,28,n)) # return 9


