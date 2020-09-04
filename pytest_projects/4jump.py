#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
数字串码
Author:    xurongzhong#126.com 技术支持qq群：630011153 144081101 
CreateDate: 2020-7-7 钉钉或微信pythontesting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='数字串码',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    for char in args.text:
        print(jumper.get(char, char), end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
