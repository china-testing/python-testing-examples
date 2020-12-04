#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论Q群144081101 书籍Q群6089740
# CreateDate: 2019-12-29

'''冒泡排序经典python面试题'''
def bubble_sort(items):
    change = True
    num = len(items) -1 
    while change and num > 0:
        change = False
        for i in range(num):
            if items[i] > items[i+1]:
                change = True
                items[i], items[i+1] = items[i+1], items[i]
        num -= 1
        
if __name__ == '__main__':
    l = [21,6,9,33,3] 
    bubble_sort(l)
    print(l) # return [3, 6, 9, 21, 33]
