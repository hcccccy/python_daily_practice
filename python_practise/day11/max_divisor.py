#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: max_divisor.py
Author: hccccccy
Date:2023/7/4 20:22
"""

""" 求两个正整数的最大公约数"""


def get_max_divisor(x, y):
    lis = []
    if x >= y:
        for i in range(1, y + 1):
            if x % i == 0 and y % i == 0:
                lis.append(i)
        return lis[-1]
    for i in range(1, x + 1):
        if x % i == 0 and y % i == 0:
            lis.append(i)
    return lis[-1]


print(get_max_divisor(101, 505))

""" min()函数可以返回给定参数的最小值 不用再费力判断"""


def get_max_divisor2(x, y):
    d = 1
    # 都有公约数1 再计算没有意义 从2 开始判断
    for i in range(2, min(x, y)+1):
        # 公约数判断
        while (x % i == 0) and (y % i == 0):
            # 获取当前最大公约数 继续计算
            d *= i
            x /= i
            y /= i
    return d


print(get_max_divisor2(20, 100))

