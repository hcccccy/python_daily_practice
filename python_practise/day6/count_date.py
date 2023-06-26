#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: count_date.py
Author: hccccccy
Date:2023/6/27 00:12
"""

""" 给定任意年月日 计算当年已经过去多少天"""


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def count_date(year, month, day):
    count = 0
    if is_leap_year(year):
        # 月份日数固定 可以直接定义个列表
        month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, month - 1):
        # 从0开始取下标 所以遍历month要-1
        count += month_list[i]
    count += day
    return count


print(count_date(2023, 6, 27))
