#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# slice
L = ['Micheal', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[1:3])

print(L[-1])
print(L[-2:])
print(L[-2:-1])

# generate a sequence
L = list(range(100))
print(L[:13])
print(L[10])
print(L[:10])
print(L[-10:])
print(L[:21:2])
print(L[10:20:3])
print(L[:])
print(L[::10]) # posiiton 0, then 10 position after position 0 is position 10, then 10 position after position 10 is position 20, ....

# other object can be sliced
print((0, 1, 2, 3, 4)[:3]) # tuple
print('ABCDEF'[:3]) # str
print('ABCDEF'[::2])






