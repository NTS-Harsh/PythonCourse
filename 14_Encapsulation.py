# Encapsulation mean hiding internal details of how an object works

class car:
    def __init__(self):
        self.brand = "BMW" # Public : Accessible from anywhere

class car1:
    def __init__(self):
        self._brand = "Audi" # Protected : Please don't access this outside

class car2:
    def __init__(self,name):
        self.__brand = name # Private
    
    def show(self):
        print(f"{self.__brand}")


c1 = car()
c1.brand = "Tata"
print(c1.brand) # Accessible

c2 = car1()
c2._brand = "Bugatti"

print(c2._brand) # Technically allowed
c3 = car2("Porsche")
# print(c3.__brand)
c3.show()


