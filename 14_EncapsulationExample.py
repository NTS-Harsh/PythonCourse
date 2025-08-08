# Getter and Setter methods

class Account:
    def __init__(self,balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

    def set_balance(self,amount):
        if amount >=0:
            self.__balance += amount
        else:
            print("Invalid amount")

isha = Account(1000)
print(isha.get_balance())
isha.set_balance(500)
print(isha.get_balance())

harsh = Account(2000)
harsh.__balance = 3000
# print(harsh.__balance)
print(harsh.get_balance())
