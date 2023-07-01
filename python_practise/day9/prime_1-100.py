#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: prime_1-100.py
Author: hccccccy
Date:2023/7/1 23:20
"""

""" 100 以内的素数 以空格隔开"""


def is_prime(n):
    """
    判断是否为素数
    :param n: 任意数
    :return: True or False
    """
    if n in [0, 1]:
        return False
    elif n == 2:
        return True
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def get_prime(m):
    """
    返回100内的素数
    :param m: 任意数
    :return: 区间内的素数
    """
    prime_lis = []
    for i in range(0, m + 1):
        """ 注意!! 这一步判断的是i是否为素数"""
        if is_prime(i):
            prime_lis.append(str(i))
    return ' '.join(prime_lis)


print(get_prime(100))
