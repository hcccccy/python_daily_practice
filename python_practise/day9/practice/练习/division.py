#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: division.py
Author: hccccccy
Date:2023/5/30 19:42
"""

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('You cannot divide by zero!')


while True:
    fir_num = input('\nFirst number:')
    if fir_num == 'q':
        break
    sec_num = input('Second number:')
    try:
        answer = int(fir_num) / int(sec_num)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
