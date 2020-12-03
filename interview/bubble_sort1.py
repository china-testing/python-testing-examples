#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论Q群144081101 书籍Q群6089740
# CreateDate: 2019-12-29

'''冒泡排序经典python面试题'''
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
            
if __name__ == '__main__':
    l = [21,6,9,33,3] 
    bubble_sort(l)
    print(l) # return [3, 6, 9, 21, 33]

