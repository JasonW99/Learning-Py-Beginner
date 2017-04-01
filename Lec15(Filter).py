#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter() is similar to map(). the difference is that it only keeps true and abandon the false
# pick the odd numbers
def is_odd(x):
    return x % 2 == 1
list(filter(is_odd, [1, 3, 6, 7, 0, 40]))

# remove the empty elements
def not_empty(s):
    return s and s.strip() #strip() removes space for a str at the start and in the end
list(filter(not_empty, ['', '4', 'rt', ' ', ' n']))

# find the prime number
def is_prime(x):
    if x <= 3:
        return True
    return not any([x % i == 0 for i in [2] + list(range(3, x-1, 2))])
is_prime(8)
list(filter(is_prime, range(1, 30)))
'''
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
不断筛下去，就可以得到所有的素数。
用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
'''
# a generator of a infinity odd number series(starting from 3)
def _odd_iter():
    x = 3
    while True:
        yield x
        x = x + 2

# a filtering function (a function that returning another function!!!!!!!!!!!!!!!!)
def _not_divisible(n):
    return lambda x: x % n >0

# a generator returns prime numbers
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it) # update the generator, update the RULE of the generator!!!!!
        # 'it' is the original sequence 3, 5, 7, 9, ....
        # however, the filtering rule is updated on 'it'
        # ...
        # filter(lambda x: x % 7 == 0,
        #        filter(lambda x: x % 5 == 0,
        #               filter(lambda x: x % 3 == 0, it)))

  for n in primes():
    if n < 30:
        print(n)
    else:
        break

###################################################################
# Example of updating a generator
it1 =_odd_iter()
next(it1)
it2 = map(lambda x: x + 1, it1)
next(it2)
it3 = map(lambda x: x + 1, it2)
next(it3)

list(filter(lambda x: x % 2 == 1, [4]))
list(filter(lambda x: x % 2 == 1, [5]))
###################################################################

# find palindrome number
def is_palindrome(x):
    x_inv = int(str(x)[::-1])
    return x == x_inv

def is_palindrome2(x):
    x = str(x)
    result = True
    i = 1
    while result & (i <= len(x) // 2):
        if x[i-1] != x[-i]:
            result = False
        i += 1
    return result

list(filter(is_palindrome, range(1, 100)))
list(filter(is_palindrome2, range(1, 200)))