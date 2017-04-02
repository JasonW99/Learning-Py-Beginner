#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# once we have an object, how do we know what class is this object and what method does it have?
# type() ##############################################################
'''
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
>>> type(abs)
<class 'builtin_function_or_method'>
'''

class Animal(object):
    pass
a = Animal()
'''
>>> type(a)
<class '__main__.Animal'>
'''

'''
>>> type(123)==type(456)
True
>>> type(123)==int
True
>>> type('abc')==type('123')
True
>>> type('abc')==str
True
>>> type('abc')==type(123)
False
'''

##############################################################
# other than str, int ... these basic type, how to test a function?
import types
def fn():
    pass

type(fn) == types.FunctionType
# True
type(abs)==types.BuiltinFunctionType
# True
type(lambda x: x)==types.LambdaType
# True
type((x for x in range(10)))==types.GeneratorType
# True

# isinstance() ##############################################################
# type() is not convenient to test classes
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass

a = Animal()
b = Dog()
c = Husky()
isinstance(c, Husky) # True
isinstance(c, Dog) # True
isinstance(c, Animal) # True
isinstance(b, Dog) and isinstance(b, Animal) # True
isinstance(b, Husky) # False

# isinstance() also available to test basic type
isinstance('a', str)
# True
isinstance(123, int)
# True
isinstance(b'a', bytes)
# True

# isinstance() can test either one of the given options
isinstance([1, 2, 3], (list, tuple)) # test whether is one of list and tuple
# True
isinstance((1, 2, 3), (list, tuple))
# True

# dir() ##############################################################
dir('ABC')
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',...,'upper', 'zfill']
'''

len('ABC') # 3
'ABC'.__len__() # 3

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')

    def eat(self):
        print('Eating meat...')

dir(Dog)
'''
['__class__', '__delattr__', '__dict__', '__dir__',..., 'eat', 'run']
'''

# getattr(), setattr(), hasattr()#######################################
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

hasattr(obj, 'x') # is there an attribute called 'x'
# True
hasattr(obj, 'y')
# False
setattr(obj, 'y', 19) # set an attribute named 'y' to 'obj'
hasattr(obj, 'y')
# True
print(obj.y)
# 19
getattr(obj, 'y') # get the value of the attribute named 'y'
# 19
getattr(obj, 'z') # trying to get a non-exist attribute
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'MyObject' object has no attribute 'z'
getattr(obj, 'z', 404) # if the attribute does not exist, then return the default value. in our case, '404'.
# 404

hasattr(obj, 'power')
# True
getattr(obj, 'power')
# <bound method MyObject.power of <__main__.MyObject object at 0x000001963FEF9908>>
fn = getattr(obj, 'power')
fn
# <bound method MyObject.power of <__main__.MyObject object at 0x000001963FEF9908>>
fn()
# 81

#######################################################################
# if we can write
sum = obj.x + obj.y
# then don't write
sum = getattr(obj, 'x') + getattr(obj, 'y')
# we should use the these methods like following
def readData(fp):
    pass

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None



