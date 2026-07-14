#First Class Functions

#Assigning a function to a variable
def say_hello(name):
    return f"Hello, {name}!"

greet_function=say_hello

print(say_hello("Om"))
print(greet_function("Aryan"))

#Passing function as args
def apply_operation(func, value):
    return func(value)

def double(x):
    return x*2

print(apply_operation(double, 7))

#Returning function from function
def make_multiplier(factor):
    def multiplier(x):
        return x*factor
    return multiplier

double=make_multiplier(15)
print(double(3))