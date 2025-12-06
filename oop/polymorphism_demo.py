# polymorphism_demo.py

import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Demo usage
if __name__ == "__main__":
    # Create instances
    rect = Rectangle(10, 5)
    circ = Circle(7)

    # Polymorphism in action
    shapes = [rect, circ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
