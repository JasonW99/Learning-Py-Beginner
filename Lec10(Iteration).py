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

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

##############################################################
tiangan = '甲乙丙丁戊己庚辛壬癸'
dizhi = '子丑寅卯辰巳午未申酉戌亥'

jiazi = [tiangan[x % len(tiangan)] + dizhi[x % len(dizhi)] for x in range(60)]

print(jiazi)

############################################################
print('x' + 'y')
print('x', 'y')
print('x''y')

a = [1, 2, 3]
b = [4, 5, 6]

print(a[0]+b[0])
print(str(a[0]) + str(b[0]))
