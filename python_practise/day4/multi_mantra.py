#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: multi_mantra.py
Author: hccccccy
Date:2023/6/23 01:05
"""

# 打印乘法口诀表

"""
思路:
1*1 
2*1 2*2 
3*1 3*2 3*3
......
需要两个数 a * b
a 在1-9
b 也在1-9 b需要循环a次 所以b在a的循环里

"""


def get_mantra(n):
    for i in range(1, n + 1):
        print('\n')
        for j in range(1, i + 1):
            print(f'{j}*{i}={i * j}', end=' ')


get_mantra(7)


# 递归实现

def get_mantra2(m):
    if m == 1:
        print('1*1=1')
    else:
        get_mantra2(m - 1)
        for i in range(1, m + 1):
            print(f'{i}*{m}={i * m}', end=' ')
        print()


# get_mantra2(9)
