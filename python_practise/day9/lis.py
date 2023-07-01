#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: lis.py
Author: hccccccy
Date:2023/7/1 22:44
"""

""" 列表升序"""


def lis_sort(lis):
    """
    sort 在原列表上操作
    :param lis:
    :return:
    """
    lis.sort()
    return lis


def lis_sorted(lis):
    """
    sorted 返回新列表
    :param lis:
    :return:
    """
    new_lis = sorted(lis)

    return new_lis


print(lis_sort([2, 4, 1, 5, 2, 4, ]))
print(lis_sorted([2, 4, 1, 5, 2, 4, ]))
