#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：http://t.cn/A6b9yS16 项目实战讨论Q群144081101 6089740
# CreateDate: 2020-10-15

text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]
print(w)