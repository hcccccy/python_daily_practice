#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: fibonacci.py
Author: hccccccy
Date:2023/6/28 21:30
"""

""" 生成fibonacci数列"""


# 递归实现

def fib(n):
    for i in range(1, n + 1):

        if n in [1, 2]:
            return 1
        return fib(n - 1) + fib(n - 2)


def get_fib(m):
    lis = []
    for i in range(1, m + 1):
        print(fib(i))


get_fib(10)


# 递推实现

def fib2(o):
    lis = [1, 1]
    if o < 2:
        return lis[o - 1]
    for i in range(2, o):
        lis.append(lis[i - 1] + lis[i - 2])

    return lis


print(fib2(10))