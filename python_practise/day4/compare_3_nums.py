#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: compare_3_nums.py
Author: hccccccy
Date:2023/6/23 00:13
"""

# 比较三个数的大小 利用列表的sorted
"""
sort 与 sorted 区别：

sort 是应用在 list 上的方法，属于列表的成员方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
sort使用方法为ls.sort()，而sorted使用方法为sorted(ls)
"""


def comp_3_nums(a, b, c):
    list1 = [a, b, c]
    list1.sort()
    # sort()是列表的方法 直接在原列表处理 没有返回值
    return list1[0], list1[1], list1[2]


print(comp_3_nums(10, 7, 34))


def comp_3_nums2(a, b, c):
    list1 = sorted([a, b, c])
    # sorted是内置函数 返回新的list 需要接收
    return list1


print(comp_3_nums2(10, 7, 34))
