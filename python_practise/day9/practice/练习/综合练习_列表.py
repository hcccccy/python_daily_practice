#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 综合练习_列表.py
Author: hccccccy
Date:2023/5/18 22:46
"""



list1 = [1, 2, 3, 'a', 'b', 'c', 'a', 'b', 'c', 3, 2, 1]
# list2 = list1.copy()
# 加：
# list.append('abc')  # 按顺序添加元素 无返回值
# print(id(list1))
# list1.append('abc')
# print(id(list1))
# print(list1)

# list.insert(0, 'abc')  # 将参数2添加到列表参数1的位置上

# list1.insert(1, '123')
# print(list1)

# list.extend(dict)  # 将可遍历的参数遍历后加入列表 默认遍历的是keys

# dic1 = {
#     'name': 'hcy',
#     'age': '28'
# }
# list1.extend(dic1)

# print(list1)


# # 减：
# list.pop()  # 默认将列表的最后一个元素去除并返回去除的元素，也可以以传入的索引去除元素 有返回值
#
# pop_list = list1.pop(0)
# print(pop_list)
# print(list1)

# del list[2]  # 根据索引去除元素

# del list1[-1]
# list.remove('ni')  # 根据传入的元素名称去掉一个元素

# list1.remove('123')

# # 排序：
# list.sort(reverse=True)  # 重新排序改变list数据，默认为升序
list2 = []

for i in list1:
    if isinstance(i, str):
        list2.append(i)
for i in list2:
    list1.remove(i)

print(list1)
# """
# 注意!!!不可以直接在原列表上删除,当删除一个元素,后续元素会补上,导致跳格删除
# 解决方法,遍历原列表,删除copy就好
# """
# print(list2)
# list2.sort()
# # sorted(list1, reverse=True)  # 重新排序不改变list数据，默认为升序
# sorted(list2)
#
# # list.reverse()  # 翻转列表，直接在原数据上操作 无返回值,需要查看原数据才知道有没有更改
# print(id(list2))
# list2.reverse()
# print(id(list2))
# # list(reversed(list))  # 翻转列表，有返回值,返回迭代器对象,需要遍历提取数据
# list(reversed(list2))

# # 其他；
# list.count('i')  # 返回list中的参数个数

# print(list1.count('a'))

# list.index('i', 1, 4)  # 返回参数在索引区间的索引

# print(list1.index('a', 4, -1))
# list.clear()  # 清空list里的数值，改变原数据


# list1 = list.copy()  # 浅拷贝
#
# # 遍历语句：
# for i, value in enumerate(list):
#     print(i, value)

# for i in list1:
#     print(i)

# # 列表推导式：
# list = [i for i in range(100)]


# list2 = [i + 1 for i in range(100) if i % 2 == 1]
# print(list2)
#
# list_1 = [1, 2, 3, 4]
#
# a = [(i, j, k) for i in list_1 for j in list_1 for k in list_1 if (i != j) and (i != k) and (j != k)]
# print(len(a))
# print(a)
