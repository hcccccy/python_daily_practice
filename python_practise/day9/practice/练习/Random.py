#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: Random.py
Author: hccccccy
Date:2023/5/28 21:10
"""

import random


class Die:

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


if __name__ == '__main__':
    # die_6 = Die(6)
    # for i in range(11):
    #     die_6.roll_die()
    die_10 = Die(10)
    for i in range(11):
        die_10.roll_die()
    # die_20 = Die(20)
    # for i in range(11):
    #     die_20.roll_die()
