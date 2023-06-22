#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: get_prime_again.py
Author: hccccccy
Date:2023/6/23 00:23
"""


# 找出a b区间内的素数

# 判断一个数是否为素数
def is_prime(i):
    if i < 2:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


# 是 返回 否 跳过
def get_prime_again(a, b):
    lis = []

    for i in range(a, b + 1):
        if is_prime(i):
            lis.append(i)
    return lis


# 输出素数

print(get_prime_again(0, 100))
