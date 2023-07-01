#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: write_message.py
Author: hccccccy
Date:2023/5/29 20:59
"""

file_name = 'programming.txt'

with open(file_name, 'w') as file_obj:
    file_obj.write('Now you see me\n')
    file_obj.write('Now you see me again')


# with 会自动关闭文件, 再读取需要重新打开
# with open(file_name) as file_obj2:
#     print(file_obj2.read())
