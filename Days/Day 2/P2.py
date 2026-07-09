#Example of an Abstract Base Class

from abc import ABC, abstractmethod

# Base Class
class Shape(ABC):
    @abstractmethod #Decorator
    def area(self):
        pass

    @abstractmethod  #Decorator
    def perimeter(self):
        pass
    
    # Concrete method
    def description(self):
        return f"This shape has area {self.area():.2f}"

# Child Class
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2

    def perimeter(self):
        return 2*3.14*self.radius
    
circle = Circle(5)
print(circle.area())
print(circle.perimeter())
print(circle.description())