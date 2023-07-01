#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 排列组合.py
Author: hccccccy
Date:2023/5/17 11:18
"""

# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列
list_1 = [1, 2, 3, 4]

a = [(i, j, k) for i in list_1 for j in list_1 for k in list_1 if (i != j) and (i != k) and (j != k)]
print(len(a))
print(a)
# list_2 = []
# for i in list_1:
#     for j in list_1:
#         for k in list_1:
#             if (i != j) and (i != k) and (j != k):
#                 list_2.append([i, j, k])
# print(list_2)
# print(len(list_2))

# a = [(i,j,k) for i in list_1 for j in  ]
