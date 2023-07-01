#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: range.py
Author: hccccccy
Date:2023/6/30 20:51
"""

"""基于生成器实现range"""


class Xrange:
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        count = 0
        while count < self.max_num:
            yield count
            count += 1


obj = Xrange(100)
for i in obj:
    print(i)
