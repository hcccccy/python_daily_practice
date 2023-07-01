#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: new_project
File: 综合练习_字符串.py
Author: hccccccy
Date:2023/5/18 21:05
"""

from demo.练习.函数 import greet



dig_str = '   123 123 11 22 33   '

eng_str = '    abc hello Hello Hello HELLO    '

chi_str = '   你好, 我是测试字符  '

mix_str = '1111   你好, 你好 我是测试字符 这是数字 123445745 11 22 33 这是英文 abc aa bb cc dd hello world HELLO WORLD  1111'

# str.upper()  # 所有字符大写 支持中英文 有返回值 需要定义变量接收

# r = mix_str.upper()
#
# print(r)

# str.lower()  # 所有字符小写(支持中英)
# r1 = mix_str.lower()
#
# print(r1)


# str.casefold()  # 所有字符小写 （支持中英及很多不同种类的语言）

# r2 = mix_str.casefold()
# print(r2)


# str.title()  # 首字母大写（每个单词首字母）

r3 = mix_str.title()

# print(r3)

# str.capitalize()  # 首字母大写（字符串首字母）
# r4 = eng_str.strip().capitalize()
# print(r4)


# str.count('i', start, stop)  # 字符串出现的次数

r5 = mix_str.count('o')

# print(r5)


# str.find('i', start, stop)  # 返回字符串的索引，若没有则返回-1

r6 = mix_str.find('o')

# print(r6)


# str.index('i', start, stop)  # 返回字符串的索引，若没有则   报错!!!!报错注意!!!!

r7 = mix_str.index('o')

# print(r7)

# str.rfind('i')  # 类似于find()，不过是从右边开始查找

r8 = mix_str.rfind('o')

# print(r8)
# str.rindex('i')  # 类似于index()，不过是从右边开始查找


# '+'.join(list)  # 字符串作为分隔符插入字符串或列表中

r9 = ','.join(eng_str.split(' '))
# print(r9)


# str.split('i')  # 用分隔符拆分字符串，默认以'\n'分隔

# r9 =','.join(eng_str.split(' '))


# str.splitlines()  # 用换行符拆分字符串，不需要传入参数


# r10 = eng_str.splitlines()
#
# print(r10)


#
# str.replace(old, new, [count])  # 替换指定的字符串

r11 = mix_str.replace('你', ' 我不', 1)
# print(r11)


# str.count(sub, start=0, end=len(string))  # 统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

r12 = mix_str.count(' ', 0, 20)

# print(r12)


# str.startswith('Ni')  # 检查字符串是否以传入参数值开头 返回True or False

r13 = mix_str.startswith('我')
# print(r13)


# str.endswith('hui')  # 检查字符串是否以传入参数值结尾 同上

r14 = mix_str.endswith('d')
# print(r14)


#
# str.ljust(10, '#')  # 返回原字符左对齐，并使用空格填充至长度为参数的新字符串

r15 = dig_str.ljust(20, ' ')
# print(r15)

# str.rjust(10, '#')  # 返回原字符右对齐，并使用空格填充至长度为参数的新字符串
# str.center(10, '#')  # 返回原字符居中，并使用空格填充至长度为参数的新字符串

# str.lstrip('hui')  # 删除字符串左边含有参数的字符，参数默认为空格
# str.rstrip()  # 删除字符串右边含有参数的字符，参数默认为空格
# str.strip()  # 删除字符串左右两边含有参数的字符，参数默认为空格


r16 = mix_str.strip('1111')

# print(r16)


# str.partition('jia')  # 把字符串以传入参数分割成三部分,参数前、参数、后，返回三个元素的元组
# ('1111   ', '你好', ', 你好 我是测试字符 这是数字 123445745 11 22 33 这是英文 abc aa bb cc dd hello world HELLO WORLD  1111')
r17 = mix_str.partition('你好')

# print(r17)

# str.rpartition('jia')  # 类似于 partition()函数,不过是从右边开始.


# list = eval("['a','b','c']")  # 返回去掉双引号后的数据

# r18 = eval("")
# print(r18)


# str.isalpha()  # 是否都是字母

r19 = eng_str.replace(' ', '').isalpha()
# print(r19)

# str.isdigit()  # 是否都是数字

# r20 = dig_str.replace(' ', '').isdigit()

# str.isalnum()  # 是否都是字母或数字


# str.isspace()  # 是否都是空格
# str.isupper()  # 是否都是大写
# str.islower()  # 是否都是小写
# str.istitle()  # 是否开头是大写


# isinstance('nijiahui', str)  # 参数1的数据类型是否和参数2一致
r20 = isinstance({1}, set)
# print(r20)

my_str = " [1,2,3]"

r = eval(my_str)  # 简单来说就是把字符串的双引号去掉
# print(r)


# 字符串的增删改查

# 增

# add = dig_str + eng_str
# print(add.replace(' ',''))

name = 'hcccccy'
age = '28'
height = '1.75m'

info= f'我是{name}, 我{age}了, 身高是{height}'

print(info)

