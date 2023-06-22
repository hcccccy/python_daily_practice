#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: factorial.py
Author: hccccccy
Date:2023/6/21 21:21
"""

# 求一个数的阶乘

"""方法1 for 循环"""


def get_factorial(n):
    fac1 = 1
    for i in range(1, n + 1):
        fac1 *= i
    return fac1


# print(get_factorial(5))

"""方法2 while循环"""


def get_factorial2(m):
    fac2 = 1
    while m > 0:
        fac2 *= m
        m -= 1
    return fac2


# print(get_factorial2(5))

"""方法3 递归"""


def get_factorial3(o):
    fac3 = 1
    if o < 1:
        return 1
    fac3 *= get_factorial2(o)
    return fac3


print(get_factorial3(4))


def get_factorial4(p):
    if p == 1:
        return 1
    return p * get_factorial4(p - 1)


print(get_factorial4(4))

"""
拓展
python3 range返回对象而不是列表 要用list迭代出数据
"""
# 创建一个1-20的列表

# lis = list(range(21))
