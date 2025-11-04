from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * 3.14  * 2
    

class Square(Shape):
    def __init__(self, sidelength):
        self.sidelength = sidelength

    def area(self):
        return self.sidelength ** 2


a = Rectangle(10, 5)
b = Circle(5)
c = Square(5)

