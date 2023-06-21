#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: 2,list_get_sum.py
Author: hccccccy
Date:2023/6/20 00:50
"""

# 求列表中所有项的和

from functools import reduce

list1 = [1, 2, 1, 3]
"""
用传给 reduce()中的函数 (这里就是lambda x,y 这个匿名函数)（有两个参数 x,y）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
lambda 匿名函数, 不需要指定函数名,直接写方法

"""
print(reduce(lambda x, y: x + y, list1))

"""其他扩展高阶函数
1,map() 映射, 接收的参数也是一个函数和一个可迭代对象, 会将迭代对象中的每个元素调用函数
返回一个对象,需要用list迭代出数据
"""


def double_num(n):
    return n * 2


# [2, 4, 2, 6]

print(list(map(double_num, list1)))
# ['1', '2', '1', '3']

print(list(map(str, list1)))

""" 
filter() 接收函数和可迭代对象,筛选条件后返回值
"""


def get_odd(n):
    if n % 2 != 0:
        return n


# [1, 1, 3]
print(list((filter(get_odd, list1))))


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

# 直接sum(可迭代对象,总数再加上这个数字)
print(sum(list1, 1))
# -->8
