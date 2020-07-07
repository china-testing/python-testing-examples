#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com 技术支持qq群：630011153 144081101 
# CreateDate: 2020-7-7 钉钉或微信pythontesting

import random


def guessing_game():
    """
    生成一个从1到100的随机整数。
    反复要求用户猜测这个数字。直到猜对为止，没猜对时告诉高了或低了。
    """
    answer = random.randint(0, 100)

    while True: 
        user_guess = int(input('请输入一个数字: '))
        if user_guess == answer:
            print(f'恭喜你，猜对了。 中奖号是{user_guess}')
            break
        if user_guess < answer:
            print(f'{user_guess}偏低了!')
        else:
            print(f'{user_guess}高了!')
            
if __name__ == '__main__':
    guessing_game()