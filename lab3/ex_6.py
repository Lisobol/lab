#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = None

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open('G:\РИП\lab4-master\lab4-master\data_light_cp1251.json') as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов


#@print_result
def f1(arg):
    return list(set([((arg[i]['job-name']).lower()) for i in range(len(arg))]))

f1(data)


#@print_result
def f2(arg):
    return list(filter((lambda x: x if x.startswith("программист") else None),arg))


#@print_result
def f3(arg):
    return list(map(lambda x:x+' c опытом Python', arg))


@print_result
def f4(arg):
    a = list()
    [a.append('{},зарплата {}руб'.format(x, y)) for x, y in zip(arg, [x for x in gen_random(100000, 200000, len(arg))])]
    return a


with timer():
    f4(f3(f2(f1(data))))
# a=[1,2,3,4,5]
# @print_result
# def f5(arg):
#     a=[1,2,3,4,5]
#     return list(map(lambda x:x**3,a))
#
# f5(a)
#
#
# @print_result
# def f6(arg):
#     a=[x**3 for x in arg]
#     return a
#
#
# f6(a)