# -*- coding: utf-8 -*-
# if
age = 20
if age >= 18:
    print('your age is:', age)
    print('adult')

# if else
age = int(input()) # note the return value of input() is a str, we need to convert it to int
if age >= 18:
    print('your age is:', age)
    print('adult')
else:
    print('your age is:', age)
    print('teenager')


# if elif else
age = int(input())
print('your age is:', age)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
elif age >= 1:
    print('kid')
else:
    print('are you kidding me >_<?')

# if x, as long as x is non-zero number or non-empty string or non-empty list, x is treated as True. otherwise, x is treated as False.
x = input('input some X')
if x:
    print('True')

