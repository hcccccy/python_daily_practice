#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: 4 high level func.py
Author: hccccccy
Date:2023/7/3 15:30
"""

""" 四个常用的高阶函数"""

""" 1 lambda 匿名函数 不需要声明函数名 可以放在表达式里"""


def total(a, b):
    return a + b


print((lambda x, y: x + y, 1, 2))

# 待解决 flist[0]是什么
flist = [lambda x: x * x for x in range(1, 3)]


"""
map()映射  接收一个函数和一个可迭代对象, 调用迭代对象中的元素传入函数
可配合lambda使用
"""

lis = [1,2,3,4]
print(list(map(lambda x: x * 2, lis)))

