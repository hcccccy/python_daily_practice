#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 综合练习_集合.py
Author: hccccccy
Date:2023/5/19 15:17
"""

# 不能出现可变的数据类型。
# 保存的元素是唯一的。(与dict中的key相似)
# 1，定义
#     1) set = set()
#     2) set = {1,2...}

set_1 = set()
set_2 = {1, 2, 3, 'a', 'b', 'c'}
# 2，增加元素
#     1) set.add('sub')    # 将sub作为整体加入集合 无返回值, 直接在原集合上更改
set_1.add('abc')
# print(set_1)

#     2) set.update('sub') # 将sub遍历加入集合
set_1.update('abc')

lis = [1, 2, 3]
set_1.update(lis)
# print(set_1)

# 3，删除元素
#     1) set.remove('sub')   # 将元素sub移除集合中（若无则报错）
# set_1.remove('a')
# set_1.remove('z')


#     2) set.discard('sub')  # 将元素sub移除集合中（若无，无操作）
set_1.discard('z')

#     3) set.pop()           # 随机删除一个元素，并将其返回（没有参数）
set_1.add('test')
# print(set_1.pop())

# 4，in /  not in / for
# 5,其他
#     1）set.clear()
#     2）set.copy()
#     3）不可变集合：set=frozenset(set)
#
# 6,功能：
#     1）去重
#     set = set(list)
#     2）交集
a = [0, 1, 2, 3, 4]
b = ['a', 9]
#         1) set = set1 & set2

# 交集
# print(set(a) & set(b))

#         2) set = set1.intersection(set2)
# print(set(b).intersection(set(a)))


#     3）并集
#         1) set = set1 | set2

# print(set(a) | set(b))
#         2) set = set1.union(set2)
# print(set(b).union(set(a)))

#     4）差集
# a中有而b中没有 a-b
# print(set(a) - set(b))

# b中有而a中没有 b-a
# print(set(b) - set(a))

#         1) set = set1 ^ set2
# (a - b) + (b - a)
# print(set(a) ^ set(b))


#         2) set = set1.difference(set2)

# print(set(a).symmetric_difference(set(b)))
#     5）判断

#         set1.issubset(set2)
# print(set(b).issubset(set(a)))
#         set1.issupperset(set2)
# print(set(a).issuperset(set(b)))

#         set1.isdisjoint(set2) 判断两个集合是否有相同的元素 有返回false 没有返回true 反人类嘛这不是!!!!!!

print(set(a).isdisjoint(set(b)))

# print(set_1)
