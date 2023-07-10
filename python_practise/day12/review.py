#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: review.py
Author: hccccccy
Date:2023/7/9 21:00
"""
""" 求一个数的阶乘"""
total = 1
for i in range(1, 5):
    total *= i
# print(total)

""" 求区间内的素数"""


def is_prime(i):
    if i == 1:
        return False
    elif i == 2:
        return True
    for j in range(3, i):
        if i % j == 0:
            return False
    return True


def get_prime(n):
    lis = []
    for i in range(1, n + 1):
        if is_prime(i):
            lis.append(i)
    return lis


# print(get_prime(20))


"""打印九九乘法表"""

# for i in range(1, 10):
#     print('\n')
#     for j in range(1, i + 1):
#         print(f'{j}*{i}={i * j}', end=' ')

"""求1000以内的所有完数"""

for i in range(1, 1001):
    t = 0
    for j in range(1, i):
        if i % j == 0:
            t += j
    if t == i:
        print(i)

"""生成斐波那契数列"""


def fib(num):
    for i in range(1, num + 1):
        if num in [1, 2]:
            return 1
        return fib(num - 1) + fib(num - 2)


def get_fib(n):
    for j in range(1, n + 1):
        print(fib(j))


get_fib(10)
