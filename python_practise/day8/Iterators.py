#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: Iterators.py
Author: hccccccy
Date:2023/6/30 18:49
"""

""" 迭代器和生成器的理解 """

""" 迭代器

1 迭代函数 函数中包含__iter__(返回本身) , __next__(迭代下一个数据)

2 可迭代对象 内部包含__iter__方法 返回一个迭代函数 

3 可迭代对象内都包括了一个迭代函数 用 可迭代对象.__iter__(), 就能得到迭代函数

4 迭代函数都含有__next__ 所以可以用for循环进行迭代 

5 __next__会遍历返回下一个数据并记录当前遍历位置 当数据遍历完成后会抛出StopIteration 遍历结束

"""


# 创建一个迭代器类

class Iter:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > 3:
            raise StopIteration
        return self.count


# 生成迭代器对象

it = Iter()
# print(it.__next__())  # next(it) 同样效果
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
""" 
输出结果
1
2
3
Traceback (most recent call last):
  File "F:\桌面\github_python\python_practise\day8\Iterators and generators.py", line 49, in <module>
    print(it.__next__())
  File "F:\桌面\github_python\python_practise\day8\Iterators and generators.py", line 40, in __next__
    raise StopIteration
StopIteration

"""
it2 = Iter()

# for循环先调用__iter__ return self 所以还是Iter类本身 之后一直调用__next__ 迭代出数据赋值给i
# for i in it2:
#     print(i)


"""--------------------------可迭代对象---------------------------"""


class Iter_obj:
    def __iter__(self):
        return Iter()


# 可迭代对象中没有__next__ 但是通过__iter__ 返回了一个迭代器对象（包含__next__）多了一层
obj = Iter_obj()

for i in obj:
    print(i)
