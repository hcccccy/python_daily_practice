#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: pi_string.py
Author: hccccccy
Date:2023/5/29 20:28
"""

file_name = 'pi_million_digits.txt'

with open(file_name) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
# print(pi_string[:100] + '...')
# print(len(pi_string))

birth = input('请输入您的生日,格式为mmddyy:')

if birth in pi_string:
    loc = len(pi_string.split(birth)[0])
    print(f'你的生日在圆周率前100w位中的第{loc}位')
    print(pi_string[loc:loc + 6])
else:
    print('你的生日不在圆周率前100w位中')

