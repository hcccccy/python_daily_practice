#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 函数.py
Author: hccccccy
Date:2023/5/25 14:44
"""


def greet(username):
    """ 打个招呼吧"""
    print('hello! ' + username.title())


def describe_city(city_names, from_country='China'):
    """ 返回城市所属国家"""
    for city_name in city_names:
        if city_name == 'london':
            city_name.capitalize()
            from_country = 'England'
            print(city_name + ' is in ' + from_country)

        else:
            city_name.capitalize()
            print(city_name + ' is in ' + from_country)


def sandwich(*toppings):
    print('Making a sandwich with the following toppings:')
    for topping in toppings:
        print('-' + topping)


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


def make_car(producer, model, **car_infos):
    car_info = dict()
    car_info['producer'] = producer
    car_info['model'] = model
    for k, v in car_infos.items():
        car_info[k] = v

    print('Your car_info:', car_info)


if __name__ == '__main__':


    make_car('subaru', 'outback', color='blue',tow_package=True)

    # user_profile = build_profile('hu', 'changye', age=28, height=1.75, skill='python')
    # print(user_profile)
    # greet('harry')
    # city_list = ['nanjing', 'chuzhou', 'london']
    # describe_city(city_names=city_list)
    # sandwich('mushrooms', 'green peppers', 'extra cheese')
    # sandwich('rice', 'egg')
    # sandwich('a', 'b', 'c', 'd', 'e')
