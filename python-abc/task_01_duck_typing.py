#!/usr/bin/env python3
"""
Define abstract Shape class and implement
Circle and Rectangle using duck typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all shapes"""

    @abstractmethod
    def area(self):
        """Returns the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Returns the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle shape with radius"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape with width and height"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape (using duck typing)"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
