#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: review2.py
Author: hccccccy
Date:2023/7/3 14:58
"""
from functools import reduce

"""1 编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。"""


def get_nums(begin, end):
    lis = []

    for i in range(begin, end + 1):
        if i % 7 == 0 and i % 5 != 0:
            # join方法只有能用于字符串 i是数字 所以需要str(i)转换类型
            lis.append(str(i))

    return ','.join(lis)


""" 2 求列表中所有项的和 """


def get_lis_sum(lis):
    return sum(lis)


def get_lis_sum2(lis):
    total = 0
    for i in range(0, len(lis)):
        total += lis[i]
    return total


# lambda实现
# from functools import reduce
lis1 = [1, 2, 3, 4]

"""
reduce()接受函数(这里就是lambda x,y 这个匿名函数)（有两个参数 x,y）先对集合中的第 1、2 个元素进行操作，
"""
total = reduce(lambda x, y: x + y, lis1)

if __name__ == '__main__':
    # print(get_nums(2000, 3200))

    print(get_lis_sum(lis1))
    print(get_lis_sum2(lis1))
    print(total)