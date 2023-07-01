#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: generators.py
Author: hccccccy
Date:2023/6/30 19:23
"""

""" 生成器"""

""" 先理解yield

在函数中使用了yield关键字就会把函数变成一个生成器

yield相当于一个可以暂停程序运行的return 


"""


def gen():
    print('start')
    yield 1
    print('-' * 20)
    yield 2


# 生成器对象
g = gen()
# print(next(g))  # 输出 start 1
# print(next(g))  # 输出 -------------------- 2

# 支持next() 支持__next__
# print(next(g))
# print(next(g))

""" for循环调用顺序  先调用可迭代对象中的__iter__方法  会返回一个迭代器对象  继而调用迭代器对象中的__next__"""

""" 可迭代对象中是没有__next__的 但是会通过__iter__返回一个迭代器对象（包含__next__） 多一层调用"""


# 支持 for循环
for i in g:
    print(i)
