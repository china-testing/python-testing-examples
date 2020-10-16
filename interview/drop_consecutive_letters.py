#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/china-testing/python-testing-examples 
# interview/drop_consecutive_letters.py
# 项目实战讨论Q群144081101 6089740
# CreateDate: 2020-10-16

def no_consecutive_letters (s):
    return s[0] + ''.join(s[i] for i in range(1,len(s)) if s[i] != s[i-1])

print(no_consecutive_letters("PPYYYTTHON"))
print(no_consecutive_letters("PPyyythonnn"))
print(no_consecutive_letters("Java"))
print(no_consecutive_letters("PPPHHHPPP")) 
