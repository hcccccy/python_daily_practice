#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: sum_nums.py
Author: hccccccy
Date:2023/6/21 15:21
"""

# 两数之和
num1 = 100
num2 = 200


# 1
def sum_nums(n, m):
    print(n + m)


# sum_nums(num1, num2)

# 2 sum()传入可迭代对象
lis = [num1, num2]

# print(sum(lis))

# ------------------------------------------------------------
# 3 扩展 eval(字符串(序列，可迭代)表达式)
str1 = '100+200'
str2 = '[1,2,3]'
str3 = "{'name':'hcy', 'age':28}"
print(eval(str1))

# better
print(eval('num1+num2'))  # 300

print(eval(str2))  # [1, 2, 3]

print(eval(str3))  # {'name': 'hcy', 'age': 28}
