#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: theorem.py
Author: hccccccy
Date:2023/7/4 21:04
"""

""" 定理 两数之积 = 最大公约数 * 最小公倍数"""


def theorem():
    a = int(input('please enter 1st num:'))
    b = int(input('please enter 2nd num:'))
    s = a * b
    while a % b != 0:
        a, b = b, (a % b)
    else:
        print("最大公约数是：", b)
        print("最小公倍数是：", s // b)
