#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: class_electriccar.py
Author: hccccccy
Date:2023/5/27 17:43
"""

from demo.练习.class_car import Car


class Battery:
    """电瓶属性"""

    def __init__(self, battery_size):
        self.battery_size = battery_size

    def des_battery_size(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        range_dis = 0
        if self.battery_size == 70:
            range_dis = 240
        elif self.battery_size == 85:
            range_dis = 300

        message = "This car can go approximately " + str(range_dis) + " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """电动汽车类"""
    """这是子类自己的属性 可以比父类多"""

    def __init__(self, make, model, year, battery_size):
        """python3 super()不需要传参 会自动继承"""
        super().__init__(make, model, year)
        """电池属性 相当于把battery类作为电动车类的一个属性,但同时它还是个类,包含类的一切功能"""
        self.battery = Battery(battery_size)

    def fill_gas_tank(self, volume):
        print('ElectricCar has no tank')


if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2020, 70)
    print(my_tesla.get_descriptive_name())
    my_tesla.fill_gas_tank('70')

    """battery是电动汽车的私有属性,但同时也是个类, 能调用类里面的方法"""
    my_tesla.battery.des_battery_size()
    """同样的调用方法"""
    my_tesla.battery.get_range()
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()
