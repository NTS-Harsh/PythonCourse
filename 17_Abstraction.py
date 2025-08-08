# Hiding implementation details and showing only essential features to the user

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

c = Cat()
d = Dog()

c.sound()
d.sound()
