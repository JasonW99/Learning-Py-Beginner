#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()
# Animal is running

cat = Cat()
cat.run()
# Animal is running

################################################################
class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running')

dog = Dog()
dog.run()
# Dog is running
dog.eat()
# Eating meat...


cat = Cat()
cat.run()
# Cat is running

################################################################
# once we define a class, it's actually defining a data type
# there is no difference with str, list or dict

a = list()
b = Animal()
c = Dog()

isinstance(a, list) # True
isinstance(b, Animal) # False
isinstance(b, Dog) # True
isinstance(c, Animal) # True
isinstance(c, Dog) # True

# polymorphism
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
# Animal is running
# Animal is running

run_twice(Dog())
# Dog is running
# Dog is running

run_twice(Cat())
# Cat is running
# Cat is running











