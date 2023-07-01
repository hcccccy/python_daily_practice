#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 综合练习_字典.py
Author: hccccccy
Date:2023/5/19 10:11
"""

# key值不能出现可变数据类型，一般用str

# # 1. 创建并返回一个新字典
# dicts = {}.fromkeys(seq, [value])  # seq为可遍历对象，value为对应数值，默认为None

dicts = {}.fromkeys(['name', 'age', 'height'])

# print(dicts)

dicts['name'] = 'hcy'
dicts['age'] = 28
dicts['height'] = 175

dict_1 = {
    'name': 'hcy',
    'age': 28,
    'height': 17.5
}

# print(dicts)

# # 2. 遍历字典key、value
# for i, j in dict.items():  # .keys() / .values())
#     pass

# for key, value in dicts.items():
# print(key, value)

#     # 3. 删除键值对
# 1） del dict['key']  # 删除特定的键值

# del dict_1['height']
# print(dict_1)
# 2） dict.clear()  # 清空字典
# 3） key = dict.pop('key')  # 参数为必填，同时返回删除键对应的数值

# pop_k = dict_1.pop('height')
# print(pop_k)
# print(dict_1)
# 4） key, value = dict.popitem()  # LIFO last in first out 移除最后添加的数据
# dict_1['skill'] = 'python'
#
# k, v = dict_1.popitem()
# print({k: v})
# print(dict_1)
# # 4. 查键值对：
# 1) dict['key']

# print(dicts['name'])


# 2) dict.get('key', 'sub')  # 若有key返回对应value；若无key，返回sub 默认none 不会报错

# print(dicts.get('gender', 'male'))
# print(dicts)
#
# print(dicts.setdefault('gender', 'male'))
# print(dicts)

# # 5. 增加键值对：
# 1） dict['key'] = value
# 2) dict.update(age='25')
#
# # 6. 增/查键值对(工厂函数)：
# dict.setdefault('key', 'sub')  # 若有key返回对应value，若无key，返回sub并加入到dict中


# # 7. 浅拷贝
# dict1 = dict.copy()

# # 8. 直接in 查询的是dict的key
# if '' in dict:
#     pass
# # 9. 直接遍历dict时，遍历的是dict的key
# for i in dict ：
# pass

# # 10. 若需要将list去重同时保持其顺序

lis =['a', 'b', 'c', 5, 4, 3, 2, 'b', 2, 0]
# {}空字典, .fromkeys(list)将list作为key传入空字典 .keys()取出keys 返回的是dict_keys迭代器 所以不能直接用[] 要用list()取出
lis = list({}.fromkeys(lis).keys())

print(lis)