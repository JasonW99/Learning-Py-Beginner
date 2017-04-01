#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sum
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
calc_sum(1, 4, 7)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
lazy_sum(1, 4, 7)
f = lazy_sum(1, 4, 7)
print(f)
print(f())

# every time we use lazy_sum() a new function will be generated
f1 = lazy_sum(1, 4, 5)
f2 = lazy_sum(1, 4, 5)
print(f1 == f2)

# when we use lazy_sum(), the function with corresponding parameters together are returned
# this is so called 'Closure'
# which is not easy to implement as it look
# do not write for loop or changing variables in a Closure
# since the returned function will not be computed before it is called
# and at that moment, the changing variable may not be the value they supposed to be

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
# the 'f' function ony enclosed 'i', however never computed.
# when 'f' function is executed by 'f()', 'i' has already changed from 1 to 3.

f1()
f2()
f3()

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
f1()
f2()
f3()
