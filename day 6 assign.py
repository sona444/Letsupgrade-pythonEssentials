from math import *
print("Question1")
class Bank:
        def __init__(self,owner_name,balance):
            self.owner_name=owner_name
            self.balance=balance
            print("Happy Transactions!!!")
        def deposit(self):
            amount=float(input("Enter amount to be deposited"))
            self.balance+=amount
            print("Amount deposited")
            print("Current balance=",self.balance)
        def withdraw(self):
            amount=float(input("Enter amount to be withdrawn"))
            min_balance=500
            if (self.balance-amount)>=min_balance:
                d=self.balance-amount
                print("Amount Withdrawn")
            else:
                d=self.balance
                print("Minimum balance is expected..Please deposit")
            print("Current balance=",d)
b=Bank("Mr.XYZ",50000)
b.deposit()
b.withdraw()

print("Question2")
class cone:
    def __init__(self,radius,hieght):
        self.r=radius;
        self.h=hieght;
    def volume(self):
        vol=1/3*pi*(self.r**2)*self.h
        print("volume of cone=", vol)
    def surface_Area(self):
        sa=pi*self.r*(self.r+(sqrt((self.h**2)+ self.r**2)))
        print("surface area of cone=", sa)
cone=cone(2,3)
cone.volume()
cone.surface_Area()
