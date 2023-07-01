#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: class_car.py
Author: hccccccy
Date:2023/5/27 17:39
"""


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.volume = 0

    def get_descriptive_name(self):
        """介绍车的信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

        return long_name.title()

    def read_odometer(self):
        """读取里程数"""
        print("This car has " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self, mileage):
        """更新里程数"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """增加里程数"""
        self.odometer_reading += miles

    def fill_gas_tank(self, volume):
        """ 油箱容量"""
        self.volume = volume
