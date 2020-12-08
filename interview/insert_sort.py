#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论Q群144081101 书籍Q群6089740
# CreateDate: 2019-12-29

'''插入排序经典python面试题'''
def insertion_sort(items):
    for index in range(1,len(items)):
        current = items[index]
        pos = index
        while pos>0 and items[pos-1] > current:
            items[pos] = items[pos-1]
            pos = pos - 1
        items[pos] = current

if __name__ == '__main__':     
    items = [54,26,93,17,77,31,44,55,20]
    insertion_sort(items)
    print(items) # [17, 20, 26, 31, 44, 54, 55, 77, 93]  
