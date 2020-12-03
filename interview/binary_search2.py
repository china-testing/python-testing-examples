#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论Q群144081101 书籍Q群6089740
# CreateDate: 2019-12-29

def bin_search(l,low,high,item):
    if low > high:
        return None
    else:
        mid = (low + high) // 2
        value = l[mid]
        if value == item:
            return mid
        elif value > item:
            return bin_search(l, low, high-1, item)
        else:
            return bin_search(l, mid+1, high, item)

if __name__ == '__main__':
    l = list(range(1,30,3)) # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    print(bin_search(l,0,len(l)-1, 7)) # return 2
    print(bin_search(l,0,len(l)-1, 1)) # return 0 
    print(bin_search(l,0,len(l)-1, 29)) # return None

