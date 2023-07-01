#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: class_ice.py
Author: hccccccy
Date:2023/5/27 19:39
"""
from demo.练习.class_res import Restaurant


class IceCream(Restaurant):

    def __init__(self, r_name, c_type, *flavors):
        super().__init__(r_name, c_type)
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)


if __name__ == '__main__':
    blue = IceCream('aaa', 'bbb', ['1', '2', '3'])
    blue.show_flavors()