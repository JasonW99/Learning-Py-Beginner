#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# define a class like following will have a problem
# people can always change or call the variables without limit, which is not good in some cases.
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

bart = Student('Bart Sim', 88)
print(bart.score)
bart.score = 95
print(bart.score)

# to solve the problem, we can make the variables private
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('the score of %s is %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, newscore):
        if 0<= newscore <= 100:
            self.__score = newscore
        else:
            raise ValueError('bad score')

bart = Student('Bart Sim', 88)
print(bart.__name)
# AttributeError: 'Student' object has no attribute '__name'
print(bart._Student__name)
# Bart Sim
bart.get_name()
# 'Bart Sim'
bart.print_score()
# the score of Bart Sim is 88
bart.get_score()
# 88
bart.set_score(95)
bart.get_score()
# 95

'''
最后注意下面的这种错误写法：
>>> bart = Student('Bart Simpson', 98)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
'''
