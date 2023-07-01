#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: class_user.py
Author: hccccccy
Date:2023/5/26 13:48
"""


# class Cat:
#     """ 猫类 """
#     """将信息传入 告知类 这个实例也是猫"""
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#
# cat1 = Cat('夏至', 2.5, 18)
# print(cat1.name)




class User:
    def __init__(self, f_name, l_name, age, height, weight):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.height = height
        self.weight = weight
        """ 默认发色为黑色"""
        self.h_color = 'black'
        """默认学龄为0"""
        self.s_age = 0
        """ 默认登录次数0"""
        self.login_attempts = 0

    def des_user(self):
        print('your info: \n', self.f_name, self.l_name, self.age, self.height, self.weight, 'kg')

    def greet_user(self):
        # print(f'你好{self.f_name}{self.l_name},欢迎使用')
        print('你好', self.f_name, self.l_name, '欢迎使用')

    """ 修改头发颜色方法"""

    def update_h_color(self, h_color):
        self.h_color = h_color

    def update_s_age(self, s_age):
        self.s_age += s_age

    def inc_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0






if __name__ == '__main__':
    hcy = User('hu', 'changye', 28, 175, 65)
    # hcy.des_user()
    # hcy.greet_user()
    """调用方法修改默认属性"""
    # hcy.update_h_color('red')
    """直接修改默认属性"""
    # hcy.h_color = 'red'
    #
    # print(hcy.h_color)
    # hcy.update_s_age(6)
    # print(f'小学毕业啦,学龄{hcy.s_age}岁了')
    # hcy.update_s_age(3)
    # print(f'中学毕业啦,学龄{hcy.s_age}岁了')

    # hcy.inc_login_attempts()
    # hcy.inc_login_attempts()
    # hcy.inc_login_attempts()
    # hcy.inc_login_attempts()
    # print(hcy.login_attempts)
    # hcy.reset_login_attempts()
    # print(hcy.login_attempts)
    hccy = Admin('hu', 'changchangye', 28, 176, 65)
    hccy.privileges.show_privileges()
