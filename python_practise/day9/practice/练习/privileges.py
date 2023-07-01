#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: privileges.py
Author: hccccccy
Date:2023/5/28 20:10
"""

from demo.练习.class_admin import Admin

ad = Admin('hu', 'changye', 28, 175, 65)
"""Admin-->User(import)     self.privileges= Privileges() """
ad.privileges.show_privileges()