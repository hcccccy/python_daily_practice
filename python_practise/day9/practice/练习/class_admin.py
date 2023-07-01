#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: class_admin.py
Author: hccccccy
Date:2023/5/28 20:07
"""
from demo.练习.class_user import User


class Admin(User):
    def __init__(self, f_name, l_name, age, height, weight):
        super().__init__(f_name, l_name, age, height, weight)
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)
