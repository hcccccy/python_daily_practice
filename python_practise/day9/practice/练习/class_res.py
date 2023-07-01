#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: class_res.py
Author: hccccccy
Date:2023/5/27 17:17
"""


class Restaurant:

    def __init__(self, r_name, c_type):
        self.r_name = r_name
        self.c_type = c_type
        self.n_served = 0

    def des_rest(self):
        print(self.r_name, self.c_type)

    def ope_rest(self):
        print('restaurant is opening')

    def set_n_served(self, n_served):
        self.n_served = n_served

    """递增就餐人数"""

    def set_increment_number(self, p_number):
        self.n_served += p_number


if __name__ == '__main__':
    res = Restaurant('kfc', '2')
    # print(res.r_name)
    # print(res.c_type)
    # res.des_rest()
    # res.ope_rest()
    res.set_n_served(20)
    res.set_increment_number(100)
    print(res.n_served)