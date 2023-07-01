#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 综合练习_元组.py
Author: hccccccy
Date:2023/5/19 09:48
"""

a = (1, 2, 3, 'a', 'b', 'c', 1, 2, 1, 2, 1, 1)

# tuple.index('i', 1, 4)  # 返回参数1在参数2、3(左开右闭)的索引
print(a.index(3))

# tuple.count('i')  # 返回参数在元组中的个数

print(a.count('1'))

# 1，定义：
# tuple = ()
# tuple = tuple()
#
#
# 2,定义只有一个元素的元组：
# tuple = (1,)
#
#
# 3,方法：
# in / not in /  tuple.index('i',1,4)  /  tuple.count('i')
