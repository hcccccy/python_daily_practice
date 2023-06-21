#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: circle_area.py
Author: hccccccy
Date:2023/6/21 22:00
"""

# 计算圆的周长与面积 2Πr Πr*r
import math


def get_circumference(r):
    return 2 * math.pi * r


def get_area(r):
    return math.pi * r * r


print(get_circumference(10))
print(get_area(10))