#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: list_get_sum.py
Author: hccccccy
Date:2023/6/20 00:50
"""
from functools import reduce

list1 = [1, 2, 1, 3]

# reduce()实现

print(reduce(lambda x, y: x + y, list1))


# for循环实现
def get_list_sum(lis):
    total1 = 0
    for i in range(0, len(lis)):
        total1 += lis[i]
    return total1


print(get_list_sum(list1))

# while 循环实现
j = 0
total2 = 0
while j < len(list1):
    total2 += list1[j]
    j += 1
print(total2)
