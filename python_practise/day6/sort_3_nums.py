#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: sort_3_nums.py
Author: hccccccy
Date:2023/6/27 00:32
"""

""" 从小到大输出三个整数"""


def sort_3_nums(a, b, c):
    lis = [a, b, c]
    lis.sort()
    return lis


# print(sort_3_nums(3, 2, 1))


def sort_3_nums2(a, b, c):
    if a > b:
        # a <= b
        a, b = b, a
    if a > c:
        # a <= c  确定a是最小的数
        a, c = c, a
    if b > c:
        # b <= c 确定b是中间的数
        b, c = c, b
    return a, b, c


print(sort_3_nums2(3, 2, 1))
