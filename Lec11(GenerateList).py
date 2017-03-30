#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# use range to generate a sequence
list(range(1, 11))

# use for loop to generate a sequence
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 ==0])

print([m + n for m in 'ABC' for n in 'XYZ' ])

# show files in current folder
import os
print([d for d in os.listdir('.')])

# using 'for' for multiple variables
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for key, values in d.items():
    print(key, '=', values)

print([k + '=' + v for k, v in d.items()])

# lower case for all elements in a list
L = ['Hello', 'World', 'IBM', 'Apple']
print([l.lower() for l in L])

L2 = ['Hello', 'World', 'IBM', 18, 'Apple', None]
print([l.lower() for l in L2 if isinstance(l, str)])
