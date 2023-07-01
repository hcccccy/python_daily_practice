#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: output_odd.py
Author: hccccccy
Date:2023/7/1 23:12
"""

""" 输出字符串奇数位字符 (从第一位开始,非下标)"""


def get_odd_str(string):
    lis = []
    for i in range(1, len(string) + 1, 2):
        lis.append(string[i - 1])
    new_str = ''.join(lis)
    return new_str


s = 'adokjhsdfonqawlhf'

print(get_odd_str(s))
