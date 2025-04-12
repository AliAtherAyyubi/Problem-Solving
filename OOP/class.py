
# class Car:
#     brand='Toyota'  #attribute of a class
#     def __init__(self,name,color):
#         self.name= name
#         self.color=color

#     def display(self):
#         print(f'Brand:{self.name} :: Color:{self.color}')


# c=Car('Mehran','White')

# c.display()

# print(c.brand)

class Bank:
    # account_holder=

    def __init__(self,name):
        self.account_holder=name
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("insuffiecient balance")
        else:
            self.balance-=amount
            print(f"You've withdrawn {amount}.")

    def displayBalance(self):
        print('Your current balance is',self.balance)

# main 

b=Bank('Ali')

b.deposit(4000)
b.withdraw(5000)
b.deposit(40000)

b.displayBalance()