#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: perfect_num.py
Author: hccccccy
Date:2023/6/26 23:37
"""

""" 求1000以内所有完数  (自己所有因数加起来等于本身的数 如6 = 1+2+3)"""


def get_perfect_num():
    for i in range(1, 1000):
        total = 0
        for j in range(1, i):
            if i % j == 0:
                total += j
        if total == i:
            print(i)


get_perfect_num()
