#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: divisible.py
Author: hccccccy
Date:2023/6/28 22:34
"""

""" 将任意正整数分解质因数 """


def get_divisible(n):
    print(f'{n}=', end='')
    m = 2
    # 被整除为1前循环
    while n != 1:
        # 找到能整除n的质数 可能重复 所以要一直循环
        while n % m == 0:
            print(m, end='')
            # 找到一个因数后用整除后的数找下一个因数
            n /= m
            # 输出格式 最后一个因数后不用加* 所以可以在内部判断是否是最后一个因数 即不能把n整除 即在n !=1 时不成立
            if n != 1:
                print('*', sep='', end='')
        m += 1


get_divisible(100)  # -->100=2*2*5*5
