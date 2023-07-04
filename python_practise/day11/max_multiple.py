#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: max_multiple.py
Author: hccccccy
Date:2023/7/4 20:56
"""

""" 求两数的最小公倍数"""


def get_multiple(a, b):
    max_multiple = [i for i in range(1, a * b + 1) if i % a == 0 and i % b == 0][0]
    return max_multiple


print(get_multiple(20, 30))
