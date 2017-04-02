#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# suppose we have student records and want to print the related information

# Procedure Oriented Programming
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 93}

def print_score(std):
    print('the score of %s is %s' % (std['name'], std['score']))

print_score(std1)
print_score(std2)

# Object Oriented Programming
class Student(object):
    # initialize the object
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # define a method
    def print_score(self):
        print('the score of %s is %s' % (self.name, self.score))

bart = Student('Bart', 59)
lisa = Student('Lisa', 89)
XX = Student(score='wahaha', name='9999')

bart.print_score()
lisa.print_score()
XX.print_score()
