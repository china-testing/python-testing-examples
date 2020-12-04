#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论Q群144081101 书籍Q群6089740
# CreateDate: 2019-12-29

'''选择排序经典python面试题'''
def selection_sort(items):
    n = len(items)-1
    for slot in range(n):
        big = last = n - slot
        for location in range(n-slot):
            if items[location] > items[big]:
                big = location
        print(big)
        items[last], items[big] = items[big], items[last]
        
if __name__ == '__main__':        
    l = [20,30,40,90,50,60,70,80,100,110]
    selection_sort(l)
    print(l) # [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
