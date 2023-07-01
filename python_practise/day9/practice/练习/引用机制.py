#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 引用机制.py
Author: hccccccy
Date:2023/5/17 22:12
"""

import sys
a = '12345'
print(id(a))
print(sys.getrefcount('1234'))