#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战钉钉群21745728 技术支持钉钉或微信pythontesting
# CreateDate: 2021-4-15

import re
import itertools


def cases(text):
    results = []
    res = re.findall(r'\((.*?)\)', text)
    strs = ""
    for item  in re.split('\(|\)',text):
        if '|' in item:
            strs += '{}'
        else:
            strs += item
    re_lists = [item.split('|')  for item in res if '|' in item]
    products = list(itertools.product(*re_lists))

    for item in products:
        results.append(strs.format(*item))
    return results

if __name__ == '__main__':
    text = '用户名(test1|test2|test3|test4)登录，访问(主菜单|帮助),下拉(3|6|10)秒，预期(响应时间不超过3秒|js加载正常|数据正确)'
    print(cases(text))
