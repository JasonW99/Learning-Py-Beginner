#!/usr/bin/env python3
# -*- coding: utf-8 -*-

int('12345')
int('12345', base=10)
int('12345', base=8)
int('1AB45', base=16)
int('1101', base=2)

def int2(x, base=2):
    return int(x, base)
int2('101000001')

# using 'functools.partial()' help us to define above function
import functools
int2 = functools.partial(int, base=2)
int2('100010')
# is equivalent to
kw = {'base': 2}
int('100010', **kw)

max2 = functools.partial(max, 10)
max2(5, 6, 7)
# is equivalent to
args = (10, 5, 6, 7)
max(*args)

