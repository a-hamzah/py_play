import numpy as np
import math


""" Example 1"""

# The eat method of Animal class is being over-ridden in Rabbit Child Class


class Animal:
    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating grass")


Rabbit1 = Rabbit()
Rabbit1.eat()


""" Example 2"""


class Shape:
    def __init__(self):
        pass


class Square(Shape):
    def __init__(self, x):
        self.x = x

    def area(self):
        area = self.x * self.x
        return area


class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        area = self.x * self.y
        return area


square1 = Square(2)
print(square1.area())
