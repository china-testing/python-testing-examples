#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论Q群144081101 书籍Q群6089740
# CreateDate: 2019-12-29

'''经典python面试题:递归实现快速排序'''
def quick_sort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    l = [21,6,9,33,3] 
    quick_sort(l)
    print(l) # return [3, 6, 9, 21, 33]
