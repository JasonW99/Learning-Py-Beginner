#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# a class is the template of an instance, an instance is an implement of a class
class Student(object):
    pass

bart = Student()
print(bart)
print(Student)

bart.name = 'Bart Sim'
print(bart.name)

#############################################################
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

bart = Student()
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'score'
bart = Student('bart')
# TypeError: __init__() missing 1 required positional argument: 'score'
bart = Student('bart', 96)

print(bart.name)
print(bart.score)

#############################################################
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('the score of %s is %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            print('A')
        elif self.score >= 80:
            print('B')
        else:
            print('C')

bart = Student('bart', 96)
bart.get_grade()
bart.print_score()