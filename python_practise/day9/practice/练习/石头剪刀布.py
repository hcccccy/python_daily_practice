#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 石头剪刀布.py
Author: hccccccy
Date:2023/5/18 23:03
"""

import random

while True:
    player = input('请输入石头, 剪刀, 布:')

    if player not in ('石头', '剪刀', '布'):
        print('输入错误,请重新输入')
    else:
        if player == '石头':
            player = 0
        elif player == '剪刀':
            player = 1
        elif player == '布':
            player = 2

    computer = random.randint(0, 2)

    if player > computer:
        print('you win!')
        break
    elif player < computer:
        print('you lose')
    else:
        print('try again')
