#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: 1,for_nums.py
Author: hccccccy
Date:2023/6/20 02:30
"""

# 编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。

""" 参考解法 """
# list要在for循环外部定义 否则会被覆盖
lis = []
# range 左闭右开
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        lis.append(str(i))
print(','.join(lis))

""" 自己尝试 """
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')
# 这样最后一个数的结尾会多个 ',' 还是转换成字符串再用join()比较符合题目


