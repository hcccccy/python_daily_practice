#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: reverse_num.py
Author: hccccccy
Date:2023/6/26 23:21
"""

""" 反向输出四位数"""


def get_revise(n):
    # reversed_num = int(str(n)[3] + str(n)[2] + str(n)[1] + str(n)[0])
    reversed_num = int(str(n)[::-1])

    return reversed_num


print(get_revise(1234))
