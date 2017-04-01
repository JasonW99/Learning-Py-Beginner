#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# using function as an input of another function
def add_f(x1, x2, func):
    return func(x1) + func(x2)

add_f(-3, 4, abs)

# map()
print([x * x for x in range(1, 5)])

def f(x):
    return x * x
r = map(f, [1, 2, 3, 4])
print(r)
print(list(r))

# map e.g.2
list(map(str, [1, 4, 99, -3]))

# reduce()
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x1, x2):
    return x1 + x2
reduce(add, [1, 3, 4, 6, 17])

def fn(x, y):
    return 10 * x + y
reduce(fn, [1, 4, 8, 4])

# map and reduce combination
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

char2num('4')
char2num('45')
map(char2num, '456')
list(map(char2num, '456'))
reduce(fn, (map(char2num, '456')))

def str2int(s):
    def chr2int(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    def fn(x, y):
        return 10 * x + y
    return reduce(fn, map(char2num, s))
str2int('876')

# using lambda to simplify a function
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
str2int2('876')

# normalize the name style using map()
def normalize(name):
    return name[0].upper() + name[1:].lower()
list(map(normalize, ['adam', 'LiSA', 'barT']))

# production using reduce
from functools import reduce
def prod_func(input):
    return reduce(lambda x, y: x * y, input)
print('3 * 5 * 7 * 9 =', prod_func([3, 5, 7, 9]))

# using map and reduce change str to float
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2float(s):
    new_s = s.split('.')
    if len(new_s) == 2:
        decimal = 10 ** len(new_s[1])
        new_s = new_s[0] + new_s[1]
    else:
        new_s = s
        decimal = 1.0
    return reduce(lambda x, y: x * 10 + y, map(char2num, new_s)) / decimal
str2float('876.88')
str2float('876')
