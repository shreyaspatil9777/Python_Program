import pickle
import os
import pathlib

class Account:

    accNo=0
    name=""
    deposite=0
    type=""

    def createAccount(self):
        self.accountnumber= int(input("Enter Account Number : "))
        self.name= input("Enter Account Holder Name : ")
        self.type= input("Enter Account Type Current or Saving : ")
        self.deposite= int(input("Enter Amount : "))
        print("\n\n\nAccount Created")

    def showAccount(self):

        print("Account Number :",self.accountnumber)
        print("Account Holder name :",self.name)
        print("Type of account :",self.type)
        print("Balance :",self.deposite)


    def modifyAccount(self):
        print("Account Number :",self.accountnumber)
        self.name= input("Modify Account Holder Name : ")
        self.type= input("Modify Account Type Current or Saving : ")
        self.deposite= int(input("Modify Balance : "))

    def depositeAccount(self,amount):
        self.deposite +=amount

    def withdrawAmount(self,amount):
        self.deposite -=amount

    def report(self):
        print(self.accountnumber, "",self.name ,"",self.type,"",self.deposite)

    def getAccount(self):
        return self.accountnumber

    def getAccountHolderName(self):
        return self.name

    def getDeposite(self):
        return self.deposite

def introduction():
    print("\t\t#####################################")
    print("\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t#####################################")
    print("\t\t\t by Shreyas patil")
    input()

introduction()

