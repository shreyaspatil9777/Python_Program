import pickle
import os
import pathlib

class Account:

    accNo=0
    name=""
    deposite=0
    type=""

    def createAccount(self):
        self.accNo= int(input("Enter Account Number : "))
        self.name= input("Enter Account Holder Name : ")
        self.type= input("Enter Account Type Current or Saving : ")
        self.deposite= int(input("Enter Amount : "))
        print("\n\n\nAccount Created")

    def showAccount(self):

        print("Account Number :",self.accNo)
        print("Account Holder name :",self.name)
        print("Type of account :",self.type)
        print("Balance :",self.deposite)
