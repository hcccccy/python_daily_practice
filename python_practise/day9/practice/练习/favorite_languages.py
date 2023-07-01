#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: favorite_languages.py
Author: hccccccy
Date:2023/5/28 20:22
"""

from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
