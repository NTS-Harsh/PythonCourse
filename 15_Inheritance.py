# Inheritance is the process where a child class (subclass) inherits the properties(attributes) and behaviour (methods) of a parent class (Superclass)


# Types of inheritance

# 1.Single inheritance
print("Singel Inheritance")
class Parent:
    def speak(self):
        print("Speaking")

class Child(Parent):
    def walk(self):
        print("Walking")

c = Child()
c.speak()
c.walk()

# 2.Multilevel Inheritance
print("Multilevel Inheritance")
class Grandfather:
    def walk(self):
        print("Walking")

class Father(Grandfather):
    def run(self):
        print("Running")

class Child(Father):
    def play(self):
        print("Playing")

c = Child()
c.play()
c.run()
c.walk()

# 3.Multiple Inheritance

class Mother:
    def skills(self):
        print("Cooking")

class Father:
    def traits(self):
        print("Hardworking")
    
class Child(Father,Mother):
    pass

ch = Child()
ch.skills()
ch.traits()

# 4.Hierarchical Inheritance

class Parent:
    def speak(self):
        print("Speaking...")

class son(Parent):
    def talk(self):
        print("Talking")

class daughter(Parent):
    def fight(self):
        print("Fighting")

s = son()
s.speak()
s.talk()

d = daughter()
d.fight()
d.speak()

# Method Overriding

class Animal:
    def sound(self):
        print("Some sound")
    def display(self):
        print("I am animal")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()
d.display()

# Super() keyword - Used to call parent class methods inside child class

class Person:
    def __init__(self,name):
        self.name = name
    
    def show(self):
        print(f"Name : {self.name}")

class Student(Parent):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade

    def show(self):
        super().show()
        print(f"grade : {self.grade}")
        