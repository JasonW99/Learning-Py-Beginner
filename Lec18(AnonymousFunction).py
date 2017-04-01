#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list(map(lambda x: x * x, [1, 2, 3, 4, 5]))

'''
lambda x: x * x
is equivalent to 
def f(x):
    return x * x
'''

# assign to a function
f = lambda x: x * x
f
f(5)

# return a function
def build(x, y):
    return lambda: x * x + y * y

# make code look simpler
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L.sort(key=lambda x: x[1])
print(L)
