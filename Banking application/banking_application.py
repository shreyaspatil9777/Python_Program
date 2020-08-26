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

def writeAccount():
    account= Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file=pathlib.Path("account.data")

    if file.exists ():

        infile=open("account.data","rb")

        mylist= pickle.load(infile)

        for item in mylist:

            print(item.accountnumber," ",item.name," ",item.type," ",item.deposite)

        infile.close()

    else:
        print("No record")

def displaySp(num):

    file=pathlib.Path("account.data")

    if file.exists ():

        infile=open("account.data","rb")

        mylist= pickle.load(infile)

        infile.close()

        found=False

        for item in mylist:

            if item.accountnumber == num:
                print("Your account Balance is= ",item.deposite)
                found = True

    else:
        print("No record to search")

    if not found:
        print("No existing record with this number")

def depositeAndWithdraw(num1,num2):

    file=pathlib.Path("account.data")

    if file.exists ():

        infile=open("account.data","rb")

        mylist= pickle.load(infile)

        infile.close()

        os.remove("account.data")

        for item in mylist:
            if item.accountnumber ==num1:
                if num2==1:
                    amount= int(input("Enter amount to deposite :"))
                    
                    item.deposite += amount
                    print("account updated")

                elif num2==2:
                    amount=int(input("Enter amount to withdraw :"))
                    item.deposite <= amount
                    item.deposite -= amount
                    
                    

                else:
                    print("please eneter mimum amount")

    else:
        print("No record search")

    outfile =open("newaccounts.data","wb")
    pickle.dump(mylist,outfile)
    outfile.close()
    os.rename("newaccounts.data","account.data")
            
def deleteAccount(num):

    file=pathlib.Path("account.data")

    if file.exists ():

        infile=open("account.data","rb")

        oldlist= pickle.load(infile)

        infile.close()
        newlist=[]

        for item in oldlist:
            if item.accountnumber==num:
                newlist.append(item)

        os.remove("account.data")

        outfile=open("newaccounts.data","wb")

        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename("newaccounts.data","account.data")


def modifyAccount(num):
    file=pathlib.Path("account.data")

    if file.exists ():

        infile=open("account.data","rb")

        oldlist= pickle.load(infile)

        infile.close()

        os.remove("account.data")

        for item in oldlist:
            if item.accountnumber ==num:
                item.name=input("Enter Account hlder name :")
                item.type=input("Enter Account type :")
                item.deposite=int(input("Enetr the amount :"))

        outfile=open("newaccounts.data","wb")

        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename("newaccounts.data","account.data")


def writeAccountsFile(account):
    file=pathlib.Path("account.data")

    if file.exists ():

        infile=open("account.data","rb")

        oldlist= pickle.load(infile)

        oldlist.append(account)

        infile.close()

        os.remove("account.data")

    else:
        oldlist=[account]

    outfile=open("newaccounts.data","wb")

    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename("newaccounts.data","account.data")


    
    
    
####start program####                
    
abc=''
num=0

introduction()

while abc !=8:

    print("\tMAIN MENU")

    print("\t1. NEW ACCOUNT")

    print("\t2. DEPOSITE AMOUNT")

    print("\t3. WITHDRAW AMOUNT")

    print("\t4. BALANCE ENQUIRY")

    print("\t5. ALL ACCOUNT HOLDER LIST")

    print("\t6. CLOSE ACCOUNT")

    print("\t7. MODIFY ACCOUNT")

    print("\t8. EXIT")

    print("\tSelect your option 1 to 8")

    abc=input()

    if abc=="1":

        writeAccount()

    if abc=="2":
        
        
        num= int(input("\tEnter the Account NO. : "))
        depositeAndWithdraw(num,1)
         
    elif abc== "3":

        num= int(input("\tEnter the Account NO. : "))
        depositeAndWithdraw(num,2)

    elif abc == "4":
        num= int(input("\tEnter the Account NO. : "))
        displaySp(num)

    elif abc== "5":
        displayAll();

    elif abc=="6":
        num= int(input("\tEnter the Account NO. : "))
        deleteAccount(num)

    elif abc=="7":
        num= int(input("\tEnter the Account NO. : "))
        modifyAccount(num)

    elif abc=="8":
        print("\t Thanks for using banking system")

        break
    else:
        print("invalid choice")

    abc=input("Enter your choice :")
        

        
        
