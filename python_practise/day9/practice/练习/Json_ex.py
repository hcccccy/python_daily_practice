#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: Json_ex.py
Author: hccccccy
Date:2023/5/31 22:08
"""

import json

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

json_data = json.dumps(data)
print(json_data)
raw_data = json.loads(json_data)
print(raw_data)

