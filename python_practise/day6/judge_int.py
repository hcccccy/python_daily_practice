#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: judge_int.py
Author: hccccccy
Date:2023/6/26 23:59
"""
"""
如何区分小数和整数 (isinstance无法区分的情况)
"""


def get_int(n):
    # n %1 如果有余数 就是小数,否则就是整数
    if n % 1 == 0:
        return True
    return False


print(get_int(1.222))
