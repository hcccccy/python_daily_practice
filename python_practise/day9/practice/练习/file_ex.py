#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: file_ex.py
Author: hccccccy
Date:2023/5/29 21:31
"""

file_name = 'guest_book.txt'

while True:
    with open(file_name, 'a') as file_obj:
        file = input('请输入您的姓名:')
        print('输入q退出程序')

        if file == 'q':
            break
        else:
            print(f'欢迎:{file}')
            file_obj.write(file+'\n')
