#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: find_mid_num.py
Author: hccccccy
Date:2023/7/1 23:35
"""
from decimal import Decimal

""" 找出整数列表中的中位数"""


def find_mid_num(lis):
    lis.sort()
    n = len(lis)
    if n % 2 != 0:
        # 列表为总数为奇数 中位数为n/2整数部分下标 用int取
        mid_num = lis[int(n / 2)]
    else:
        # 列表总数为偶数 中位数为 n/2 和n/2 +1 两数平均值
        mid_num = (lis[int(n / 2)] + lis[int(n / 2) + 1]) / 2
    return mid_num


# l = [1, 2, 4, 5, 3]
l2 = [1, 2, 4, 5, 6, 3]
# print(find_mid_num(l))
print(round(find_mid_num(l2), 2))

# 小数输出

# 1 round函数

a = 1.232345265

print(round(a, 4))  #Out[20]: 1.2323

# 2 格式化
print('%.4f' % a)

# 3 decimal

print(Decimal(a).quantize(Decimal('0.0000')))