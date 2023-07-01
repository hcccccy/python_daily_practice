#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: test_file.py
Author: hccccccy
Date:2023/5/19 06:22
"""

from demo.练习.函数 import *

greet()



# list1 = [1, 2, 3, 'a', 'b', 'c']
# list2 = list1.copy()
# for i in list1:
#     if isinstance(i, str):
#         list2.remove(i)
#
#
# print(list2)

# a = '1,2,3,4'
# for i in a:
#     print(i)
# b = (i for i in a)
# print(list(b))

# lis = [1, 2, 3, 4, 5]
# lis.reverse()

# lis.sort(reverse=True)
# print(lis)


# import random
#
# #
# # # 定义一个列表用来保存3个办公室
# offices = [[], [], []]
# #
# # # 定义一个列表用来存储8位老师的名字
# names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# #
# for n in names:
#     index = random.randint(0, 2)
#     offices[index].append(n)
# temp_list = list()
# for o in offices:
#     if len(o) > 3:
#         for i in range(len(o) - 3):
#             temp_list.append(o.pop())
#     elif len(o) < 2:
#         o.append(temp_list.pop())
# print(offices)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
