#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: str_reverse.py
Author: hccccccy
Date:2023/7/1 22:47
"""

""" 字符串逆序"""


def get_reverse(string):
    new_string = string[::-1]
    return new_string


print(get_reverse('abcd'))
