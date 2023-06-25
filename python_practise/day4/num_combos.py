#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: num_combos.py
Author: hccccccy
Date:2023/6/23 00:43
"""

# 任意两个数之间 能组成多少个不相同且各个位置上不重复的三位数
"""
思路:

百位 四种可能 1, 2, 3, 4
十位 四种可能 1, 2, 3, 4
个位 四种可能 1, 2, 3, 4


"""


def get_num_combos(a, b):
    lis = []
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            for k in range(a, b + 1):
                if i != j and i != k and j != k:
                    # print(f"{i}{j}{k}")
                    lis.append([i, j, k])
    return lis


print(get_num_combos(1, 4))
# get_num_combos(2, 5)

