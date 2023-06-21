#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: get_prime.py
Author: hccccccy
Date:2023/6/21 22:36
"""

""" 找出两数之间所有素数"""


# 思维转换 只能被1和自身整除 换句话就是1- n-1 中的所有数都不能被n整除
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def get_prime(begin, end):
    lis = []
    for i in range(begin, end + 1):
        if is_prime(i):
            lis.append(i)
    return lis


print(get_prime(1, 30))
print(get_prime(2, 30))
print(get_prime(10, 30))
