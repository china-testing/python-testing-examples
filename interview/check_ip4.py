#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群6089740 144081101
# CreateDate: 2019-12-29

import socket

def check_ip(ipaddr):
    try:
        socket.inet_aton(ipaddr)
    except socket.error:
        return False
    else:
        return True
    
    
if __name__ == '__main__':
    
    print("check_ip('1.2.3.4')", ": ", check_ip('1.2.3.4'))
    print("check_ip('1.2.3.444')", ": ", check_ip('1.2.3.444'))
    print("check_ip('0.0.0.0')", ": ", check_ip('0.0.0.0'))
    print("check_ip('127.2.3.1')", ": ", check_ip('127.2.3.1'))