# Method overloading - Compile-time polymorphism
class Operations:
    def add(self,a,b):
        print(f"Addition : {a+b}")
    def add(self,a,b,c):
        print(f"Addition : {a+b+c}")

op = Operations()
op.add(3,4)
op.add(3,5,6)


# Method Overriding - Runtime Polymorphism
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