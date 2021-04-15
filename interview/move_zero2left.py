#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群6089740 144081101
# CreateDate: 2020-11-25
def move_zero_to_right(nums):
    insert_index = len(nums) - 1
    for i in list(range(len(nums)))[::-1]:
        if nums[i] != 0:
            nums[insert_index]=nums[i]
            insert_index-=1
    for i in range(insert_index):
        nums[i]=0

if __name__ == "__main__":        
    nums = [0,1,5,0,3,8,0,0,9]
    print("old",nums)
    move_zero_to_right(nums)
    print("new",nums)