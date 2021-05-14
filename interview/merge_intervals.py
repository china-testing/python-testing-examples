#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战钉钉群21745728 技术支持钉钉或微信pythontesting
# CreateDate: 2021-5-15

def merge_interval(ranges):
    tmp_list = ranges
    merged = [tmp_list[0]]
    for current in tmp_list:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    return merged    


if __name__ == "__main__":
    ranges = [[-25, -14], [-21, -16], [-20, -15], [-10, -7], [-8, -5], [2, 4]]
    print(merge_interval(ranges))