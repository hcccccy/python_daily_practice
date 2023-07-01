#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 字符拼接.py
Author: hccccccy
Date:2023/5/16 23:00
"""
# 给定一个字符串aStr，返回使用空格或者'\t'分割后的倒数第二个子串

# my_str = 'hello world itcast and hello itcastcpp hello'

# print(my_str.split('it')[-2])

# replace(old, new, max 替换次数)
# print(my_str.replace('hello', 'hi', ))

name = input("请输入你的姓名:")
age = input("请输入你的年龄:")
height = input("请输入你的身高(m):")
password = input("请输入你的密码:")
# gender = input("请输入您的性别:") 待改

# print("请确认您的信息:\n姓名: %s\n年龄:%s\n身高:%s\n密码:%s" % (name, age, height, password))
# print("请确认您的信息:\n姓名:{}\n年龄:{}\n身高:{}\n密码:{}".format(name, age, height, password))
print(f"请确认您的信息:\n姓名:{name}\n年龄:{age}\n身高:{height}\n密码:{password}")
