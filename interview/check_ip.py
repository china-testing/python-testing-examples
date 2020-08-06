#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群630011153 144081101
# CreateDate: 2019-12-29

import re

def check_ip(address):
    if type(address) != str:
        return False
    expression = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    if not expression.match(address):
        return False
    for number in address.split('.'):
        if number.startswith('0') and len(number) >1 :
            return False
        if int(number) < 0 or int(number) > 255:
            return False
    return True

if __name__ == '__main__':
    
    print(check_ip('1.2.3.4'))
    print(check_ip('1.2.3.444'))