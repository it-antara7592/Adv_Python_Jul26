#Example of Classes and Objects
 
class Dog: #Class
    #Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof! And it is {self.age} years old"

#Creation of an  object
myDog1 = Dog("Moti",5)
myDog2 = Dog("Moochi",2)

print(myDog1.bark())
print(myDog2.bark())