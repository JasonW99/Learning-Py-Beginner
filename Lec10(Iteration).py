#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# iterate on dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

# to verify if iterable
from collections import Iterable
isinstance('abc', Iterable)
isinstance([1, 2, 3], Iterable)
isinstance(123, Iterable)

# subscript on a list
for i, value in enumerate(['A', 'B', 'C', 'D']):
    print(i, value)



