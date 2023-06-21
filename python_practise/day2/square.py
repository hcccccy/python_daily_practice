#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: square.py
Author: hccccccy
Date:2023/6/21 14:44
"""
lis = [1, 2, 3, 4, 5]

square = list(map(lambda x: x ** 2, lis))

fin = [i for i in square if i > 10]
print(fin)
