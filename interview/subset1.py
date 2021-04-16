#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群6089740 144081101
# CreateDate: 2021-4-15

def subsets(nums):
    result = [set()]
    for num in nums:
        result += [item.copy() | set([num]) for item in result]
    return result

if __name__ == "__main__":
    print(subsets(set([1, 2, 3])))