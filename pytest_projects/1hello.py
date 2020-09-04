#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
实现参数化的Hello World!
Author:    xurongzhong#126.com 技术支持qq群：630011153 144081101 
CreateDate: 2020-7-7 钉钉或微信pythontesting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', default='World', help='Name to greet')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print('Hello, ' + args.name + '!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
