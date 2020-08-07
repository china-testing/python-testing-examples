#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群630011153 144081101
# CreateDate: 2019-12-29

from check_ip import check_ip as check

def address(s, state=()):
    result = []
    length = len(s)
    start = 1 if not state else state[-1]
    for pos in range(start,length):
        if pos not in state:
            if len(state) == 2:
                seqs = state + (pos,)
                ip_str = f'{s[:seqs[0]]}.{s[seqs[0]:seqs[1]]}.{s[seqs[1]:seqs[2]]}.{s[seqs[1]:]}'
                if check(ip_str):
                    result.append(ip_str)
            else:
                result = result + address(s, state + (pos,))
    return result
               


if __name__ == '__main__':
    
    tmp = '123425'
    print(tmp, "可能的ip有", address(tmp))