import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self._validate_sides(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def _validate_sides(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive")
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Invalid triangle sides")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self, tolerance=1e-6):
        sides = sorted([self.a, self.b, self.c])
        a, b, c = sides
        return abs(a**2 + b**2 - c**2) < tolerance

def calculate_area(shape):
    return shape.area()