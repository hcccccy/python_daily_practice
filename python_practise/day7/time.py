#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: github_python
File: time.py
Author: hccccccy
Date:2023/6/28 22:09
"""
import time

""" 暂停一秒输出"""

s = '这是第七天的练习'

for i in s:
    print(i)
    time.sleep(1)

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
