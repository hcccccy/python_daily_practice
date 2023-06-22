#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: third_edge.py
Author: hccccccy
Date:2023/6/23 00:01
"""

# 求直角三角形斜边长
# 需要用到开根方法 sqrt()
import math


def get_third_edge(a, b):
    return math.sqrt(a * a + b * b)


print(get_third_edge(3, 4))
