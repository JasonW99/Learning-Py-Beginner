#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def now():
    print('2017-07-31')

f = now
now()
f()
print('function name for now():', now.__name__)
print('function name for f():', f.__name__)

# without changing the content of the function,
# what if we want to see a log which describes the function name when we call the function?
# we can create a decorator
def log(func):
    def wrapper(*args, **kw):
        # print('we are calling a function. the name of this function is %s' % func.__name__)
        print('call %s' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('today is 2017-07-31')
# using '@log' before 'def now()' is equivalent to set 'now = log(now)'

now()
# >>> now()
# call now
# today is 2017-07-31

f = now
f()
# >>> f()
# call now
# today is 2017-07-31

# what if the decorator needs some input parameters
def log(input_text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (input_text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('the name of the function is')
def now1():
    print('today is 2017-07-31')
# using '@log(xxx)' before 'def now()' is equivalent to set 'now = log(xxx)(now)'

now1()
# >>> now1()
# the name of the function is now1()
# today is 2017-07-31

# however, this time, the name of the original function has already been changed
print(now1.__name__)

# to prevent this, we need
import functools
def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log1
def now2():
    print('wahahahhaha')

now2()


# another example
import functools
def log2(input):
    if isinstance(input, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('extra input for log is', input)
                print('start calling %s()' % func.__name__)
                result = func(*args, **kw)
                print('end calling %s()' % func.__name__)
                return result
            return wrapper
        return decorator
    else:
        @functools.wraps(input)
        def wrapper(*args, **kw):
            print('start calling %s()' % input.__name__)
            result = input(*args, **kw)
            print('end calling %s()' % input.__name__)
            return result
        return wrapper


@log2
def f1(x):
    print('doing the calculation...')
    return x * 3
# equivalent to 'log(f1)'


@log2('eee')
def f2(x):
    print('doing the calculation...')
    return x * 3
# equivalent to 'log('eee')(f2)

f1(3)
# >>> f1(3)
# start calling f1()
# doing the calculation...
# end calling f1()
# Out[84]:
# 9

f2(2)
# >>> f2(2)
# extra input for log is eee
# start calling f2()
# doing the calculation...
# end calling f2()
# Out[86]:
# 6

