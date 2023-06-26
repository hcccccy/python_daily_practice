#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: daffodil_num.py
Author: hccccccy
Date:2023/6/26 23:08
"""

""" 找水仙花 三位数 各位数立方和等于该数本身"""


def get_daffodil_num():
    for i in range(100, 1000):
        # 重点是取出各个位上的数字
        # 1 字符串取值
        # a = int(str(i)[0])
        # b = int(str(i)[1])
        # c = int(str(i)[2])

        # 2 求余取值
        # 百位 直接除100取整
        a = i // 100
        # 十位 先除100求余 得到十位和个位 再除10求整 得到十位
        b = (i % 100) // 10
        # 个位 除10求余
        c = i % 10

        if a ** 3 + b ** 3 + c ** 3 == i:
            print(i)


# get_daffodil_num()


def get_daffodil_num2():
    for i in range(100, 1000):
        a = str(i)[0]
        b = str(i)[1]
        c = str(i)[2]
        if eval(a) ** 3 + eval(b) ** 3 + eval(c) ** 3 == i:
            print(i)


get_daffodil_num2()
