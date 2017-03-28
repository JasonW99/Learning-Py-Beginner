#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# call functions
abs(-100)
max(1, 2)
int('123')
int(12.34)
float('12.34')
str(100)
bool(1)
bool(-1)
bool(0)
bool('')
bool(None)

a = abs
a(-1)

# define a function
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

my_abs(-0.5)

# empty function (pass for do nothing)
def nop():
    pass
age = 0
if age >= 18:
    pass

# check the parameters
abs('A')
my_abs('A')
my_abs(1, 2)

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad openrand type')
    if x >= 0:
        return x
    else:
        return -x

my_abs('A')

# function return two values
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print(x, y)

r = move(100, 100, 60, math.pi/6)
print(r) # the return of the move is actually a tuple

# using default parameter
def power(x, n=2):
    result = 1
    while n > 0:
        result = result * x
        n = n - 1
    return result

power(3, 0)
power(3)

# use None as the default parameter
def add_end(L=[]):
    L.append('END')
    return L

add_end([1, 3, 4])
add_end()
add_end()
add_end()

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

add_end([1, 3, 4])
add_end()
add_end()
add_end()

# using changeable parameter
def calc(numbers):
    result = 0
    for i in numbers:
        result = result + i ** 2
    return result

calc([2, 3, 4])
calc(2, 3, 4)

def calc(*numbers):
    result = 0
    for i in numbers:
        result = result + i ** 2
    return result

calc(2, 3, 4)
calc([2, 3, 4])
calc(*[2, 3, 4])   # use * to return all the element of a list


# using key word parameters
def person(name, age, **kw):
    print('name:', name)
    print('age:', age)
    print('others:', kw)

person('Bob', 14)
person('Bob', 14, city='Beijing')
person('Ken', 26, city='HOng Kong', job="Engineer")

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 20, city=extra['city'], job=extra['job'])
person('Jack', 20, **extra)

# name the key word parameter
person('Ken', 26, city='Hong Kong', job="Engineer", addr='Wahahahha')
def person(name, age, *, city='Beijing', job):
    print('name:', name)
    print('age:', age)
    print('city:', city)
    print('job:', job)

person('Ken', 26, city='Hong Kong', job="Engineer")
person('Ken', 26, job="Engineer")
person('Ken', 26)
person('Ken', 26, city='Hong Kong', job="Engineer", addr='Wahahahha')
person('Ken', 26, 'Hong Kong', "Engineer")


# comparison
# *args is a changeable parameter, it receives a tuple. **kw is a keyword parameter, it receives a dict
def f1(a, b, c=0, *args, **kw):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('args:', args)
    print('kw:', kw)

f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 4)
f1(1, 2, 3, 4, 5)
f1(1, 2, 3, [4, 5, 6])
f1(1, 2, 3, *[4, 5, 6])
f1(1, 2, 3, *[4, 5, 6], 7)
f1(1, 2, 3, 4, kw1=3)
f1(1, 2, 3, 4, kw1=3, kw2=4)
f1(1, 2, 3, 4, 5, kw1=3, kw2=4)
f1(1, 2, 3, kw1=3, kw2=4)

# kw0 is a named keyword parameter, it receives a dict
def f2(a, b, c=0, *, kw0, **kw):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('args:', kw0)
    print('kw:', kw)

f2(1, 2)
f2(1, 2, kw0=4)
f2(1, 2, 3, kw0=4)
f2(1, 2, 3, kw0=[1, 2])
# f2(1, 2, 3, kw0=*[1, 2])
f2(1, 2, 3, kw0=4, kw1=7)

ARGS1 = (1, 2, 3, 4)
KW1 = {'kw1': 9, 'kw2': 10}
f1(*ARGS1, **KW1)

ARGS2 = (1, 2, 3)
KW2 = {'kw0': 7, 'kw1': 9, 'kw2': 10}
f2(*ARGS2, **KW2)


'''
*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
'''


# recursion function
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

fact(5)
fact(1000)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

fact(5)
fact(100)


'''
汉诺塔的移动可以用递归函数非常简单地实现。

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
'''
def move(n, a, b, c):
    if n == 1:
        print(a, '--->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')


'''
calculate a^b
'''
def power(x, n):
    if n == 0:
        return 1
    interm_result = power(x, n//2)
    if n % 2 == 0:
        return interm_result * interm_result
    return x * interm_result * interm_result

power(2, 3)

'''
print every subset of a given set
'''
def print_subset(X, cur=[], index=0):
    if index == len(X):
        print(cur)
        return
    cur.append(X[index])
    print_subset(X, cur, index+1) # breaking point
    cur.pop()
    print_subset(X, cur, index+1) # breaking point

X = a b c
cur = []
index = 0


print_subset(["A", "B", "C", "D"])
print_subset(["A", "B", "C"])
print_subset(["A", "B"])
print_subset(["A"])
