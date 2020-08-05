#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群630011153 144081101
# CreateDate: 2019-12-29


def binary_search(items, item, lower=0, upper=None):
    
    if upper is None: 
        upper = len(items) - 1
        
    if lower == upper:
        return upper
    else:
        middle = (lower + upper) // 2
        if item > items[middle]:
            return binary_search(items, item, middle + 1, upper)
        else:
            return binary_search(items, item, lower, middle)
        
if __name__ == '__main__':
    
    seq = [34, 67, 8, 123, 4, 100, 95]
    seq.sort()
    print(binary_search(seq, 34)) 
    print(binary_search(seq, 100)) 