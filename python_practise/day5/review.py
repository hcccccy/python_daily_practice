#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: review.py
Author: hccccccy
Date:2023/6/25 23:34
"""
from functools import reduce
import math

"""1, 编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。"""

# def for_nums(begin, end):
#     lis = []
#     for i in range(begin, end + 1):
#         if i % 7 == 0 and i % 5 != 0:
#             lis.append(str(i))
#     return ','.join(lis)
#
#
# # print(for_nums(2000, 3200))
#
"""2, 求列表中所有项的和"""
#
# lis = [1, 2, 3, 1]
# sum = 0
# for i in range(0, len(lis)):
#     # i是下标
#     sum += lis[i]
# print(sum)
#
# sum_lis = reduce(lambda x, y: x + y, lis)
#
# print(sum_lis)
#
# # print(sum(lis))
#
"""3, 计算圆的周长与面积 2Πr Πr*r"""
#
# r = input('半径')
# l = 2 * math.pi * r
# a = math.pi * r * r


"""4, 求一个数的阶乘"""


def get_factorial(n):
    # 相乘 不能为0
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


# print(get_factorial(5))


def get_factorial2(m):
    if m == 1:
        return 1
    return m * get_factorial(m - 1)


# print(get_factorial2(5))

""" 5 找出两数之间所有素数"""


# 1 判断一个数是不是素数
def is_prime(n):
    if n in [0, 1]:
        return False
    for i in range(2, n):
        # !!! 2到n-1之间能被整除的都不是素数 !!!
        if n % 2 == 0:
            return False
    return True


# 2 找出区间内所有素数
def get_prime(begin, end):
    lis = []
    for i in range(begin, end + 1):
        if is_prime(i):
            lis.append(i)
    return lis


# print(get_prime(0, 24))

""" 6 比较三个数的大小 利用列表的sorted"""


def compare_3_nums(a, b, c):
    lis = [a, b, c]
    # lis下的方法是在原列表修改
    # lis.sort()
    # sorted()返回新的list 要接收
    lis2 = sorted(lis)
    return lis2
    # return lis


# print(compare_3_nums(1, 22, 6))

""" 7 打印乘法口诀 
1*1 = 1
1*2 = 2 2*2 =4
....
"""


# 思路: 需要两个数字, a * b    a-->1-9  b -->1-9
def get_multi(n):
    for i in range(1, n + 1):
        # a --> 1-9
        print()  # 换行 \n也行
        for j in range(1, i + 1):
            # b --> 1-9
            print(f'{j}*{i}={i * j}', end=' ')


# get_multi(9)

"""8 任意区间 能组成多少个不相同且各个位置上不重复的三位数"""


# 思路 重点是3位数 需要三个循环 每个位子上的数不重复 就可以放进列表

def get_combos(a, b):
    lis = []
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            for k in range(a, b + 1):
                if i != j and i != k and j != k:
                    # list.append() 直接将列表作为一条数据加入原列表
                    lis.append([i, j, k])
    return lis


# print(get_combos(1, 5))
# print(len(get_combos(1, 5)))

""" 9 求直角三角形斜边长 """


# 需要开根方法 sqrt
# math.sqrt()

def get_third_edge(a, b):
    c = math.sqrt(a * a + b * b)
    return c


print(get_third_edge(3, 4))
