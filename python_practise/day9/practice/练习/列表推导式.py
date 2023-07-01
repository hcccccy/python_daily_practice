#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 列表推导式.py
Author: hccccccy
Date:2023/5/17 22:34
"""

a = [i for i in range(100) if i % 2 == 1]
print(a)

b = list()
for i in range(100):
    if i % 2 == 0:
        b.append(i)
print(b)
