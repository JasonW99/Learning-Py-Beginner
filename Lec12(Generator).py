#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# generator is an algorithm created and saved at memory
L = [x * x for x in range(1, 11)] # List
print(L)

g = (x * x for x in range(1, 11)) # generator
print(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)

# Fibonacci series (function)
def fib(n):
    result = [1] * n
    if n > 2:
        for i in range(2, n):
            result[i] = result[i-1] + result[i-2]
    return result

print(fib(6))

def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib1(6)

# Fibonacci series (generator)
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib2(6)
print(g)
next(g)

g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# Pascal's triangle
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i] + L[-i-1] for i in range(len(L))]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break






