# OOP - Object Oriented Programming
# Organizes the code using objects and classes
# class : blueprint for creating objects
# objects : instance of a class
# constructor : special method called automatically when an object is created. Used to initialize the attributes
# Attributes : Data stores in the object
# Methods : Functions that belong to the class

class student:
    # Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # Method
    def show(self):
        print(f"Name:{self.name}, Age:{self.age}")

name = input("Name : ")
age = int(input("Age : "))
s1 = student(name,age)
s2 = student("Harsh",22)
print(s1.name)
s1.show()
s2.show()

# Four Pillars of OOPS : 
# 1.Encapsulation
# 2.Inheritance
# 3.Polymorphism
# 4.Abstraction

