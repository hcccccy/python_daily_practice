#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: dict_keys.py
Author: hccccccy
Date:2023/7/1 22:55
"""

""" 升序输出字典的key key 可能为字符串"""
# 问题在于如何比较数字与字符串  -->直接都转换为字符串
# str.join() 参数可以是str list tuple dict 但内部数据必须为str 不然会报错

def sorted_keys(d):
    dic_keys = []
    for i in d.keys():
        dic_keys.append(str(i))
    dic_keys.sort()
    return dic_keys


dic = {1: 'a', 3: 'c', 2: 'b', 'c': 3, 'a': 1, }

print(','.join(sorted_keys(dic)))
