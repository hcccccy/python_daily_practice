#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: file_reader.py
Author: hccccccy
Date:2023/5/28 21:58
"""
import os

file_name = r'E:\new_project\text_files\pi_digits2.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
