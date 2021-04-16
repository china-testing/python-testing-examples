#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群6089740 144081101
# CreateDate: 2021-4-15
from itertools import combinations

def subsets(nums):
    result = [set()]
    for i in range(1,len(nums)+1):
        result += list(map(set, combinations(nums, i)))
    return result


if __name__ == "__main__":
    print(subsets(set([1, 2, 3])))