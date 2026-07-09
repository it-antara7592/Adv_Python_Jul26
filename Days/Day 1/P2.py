#Example of Inheritance

#Parent class /Base class
class Animal:
    def __init__(self,name):
        self.name = name

    def makeSound(self):
        return "Some sound"
    
# Child class/ Derived class
class Cat(Animal):
    def makeSound(self):
        return f"{self.name} says ~Meow" 
    
# Child class/ derived class
class Cow(Animal):
    def makeSound(self):
        return f"{self.name} says ~Moo"    
    
cat1 = Cat("Miki") 
cow1 = Cow("Jera")

print(cat1.makeSound())
print(cow1.makeSound())