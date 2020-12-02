#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群630011153 144081101
# CreateDate: 2019-12-29

def bin_search(items,lower=0, upper=None, item=0):
    if upper is None: 
        upper = len(items) - 1
        
    if lower == upper:
        return upper
    else:
        middle = (lower + upper) // 2
        if item > items[middle]:
            return bin_search(items, middle + 1, upper,item)
        else:
            return bin_search(items, lower, middle,item)

if __name__ == '__main__':
    l = list(range(1,30,3)) # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    print(bin_search(l,0,len(l)-1, 7)) # return 2
    print(bin_search(l,0,len(l)-1, 1)) # return 0 
    print(bin_search(l,0,len(l)-1, 29)) # return None

