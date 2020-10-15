#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/china-testing/python-testing-examples 
# interview/check_string2.py
# 项目实战讨论Q群144081101 6089740
# CreateDate: 2020-10-15
import re
import argparse

def check_char(source):
    return source.isalnum()

parser = argparse.ArgumentParser(description='字符串检查',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('source', metavar='str',help='请输入要检查的字符串')
args = parser.parse_args()

print(check_char(args.source)) 
