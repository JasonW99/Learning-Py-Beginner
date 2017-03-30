#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# which data type is iterable
from collections import Iterable
isinstance([], Iterable) # list
isinstance((), Iterable) # generator
isinstance({}, Iterable) # dict
isinstance('', Iterable) # str
isinstance(123, Iterable) # int
# a generator is also an iterator. list, str and dict are all iterable. however not iterator.

# using iter() change a non-iterator to iterator
isinstance(iter('abc'), Iterable)
tmp = iter('abc')
next(tmp)

isinstance(iter([]), Iterable)

# 'for' command is equivalent to an iterator
for x in [1, 2, 3, 4, 5]:
    pass

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break

