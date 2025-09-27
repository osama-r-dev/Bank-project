import sys
from banking.bank import Bank
from banking.account import PasswordTooWeak
from banking.customer import NameTooLongException
from banking.bank import InvalidAcountInfo
from banking.customer import InvalidCharacterException
from banking.account import InvalidAmountException
from banking.account import AccountDeactivated
from banking.account import NotEnoughMoneyException
from banking.bank import CustomerNotfoundException
from banking.account import ImproperPassword

AccountDeactivated
class InvalidUserInput(Exception):
    pass

def home(bank):
   try:
      userInput = int(input("1- create account    2- login      3- exit \n"))
       
      match userInput:
          case 1:
              createNewAccount(bank)
          case 2:
              login(bank)  
          case 3:
              bank.updateData()
              print("THANKS FOR USING MY BANK!")  
              sys.exit()
   except ValueError:
     print("invalid option")           

def createNewAccount(bank):
    while True:
        try:
             userFirstName = input("First Name: ") 
             userLastName = input("Last Name: ")
             userPassword = input("password: ")
             bank.addCustomer(userFirstName,userLastName ,userPassword,0,0)
             
        except NameTooLongException as excp:
            print(excp)

        except InvalidCharacterException as excp:
            print(excp)

               
        except ValueError as excp:
            print(excp)

        except PasswordTooWeak as excp:
            print(excp)   
        except ImproperPassword as excp:
           print(excp)

        else:
         print("customer has been added")   
         home(bank)
       

def login(bank ,counter = 0):
     
     account = None
     while account == None:
        if counter == 3:
          home(bank)
        try: 
             
             userID = input("user name: ")
             userPassword = (input("password: "))
             customer = bank.login(userID,userPassword)
             senderFullName = customer.firstName +" "+ customer.lastName
             account = customer.account
             

        except InvalidAcountInfo as e:
            print(e)
            counter +=1
        except ValueError as e:
            print(e)
            counter += 1
        else:    
            
         print("Success") 
       
         
     operations(account,bank,senderFullName)    

## working on this so far
def operations(account,bank,senderFullName):
 try:
  while True:
     userInput = int(input("1- My accounts   2- Deposit   3- Withdraw  4- Transfer  -5 Home  -6 Transacitons History  \n"))
     match userInput:
          case 1:
               while True:
                try:
                 print(f""" Checking Account => Balance: {account.balanceChecking} | Savings Account => Balance: {account.balanceSavings}     1- Back""") 
                 option = int(input(""))
                 if option == 1:
                   operations(account,bank,senderFullName)
                   break
                except ValueError:
                  print("Invalid option")
          case 2:
            deposit(account,senderFullName) 
          case 3: 
            withdraw(account,senderFullName)
          case 4:
           option = int(input("1- between my accounts   2- to a customer"))
           match option:
              case 1:
                 transfer(account,senderFullName)
                 
              case 2:
                 transferToAnotherCustomer(account,bank,senderFullName)
                 
          case 5:
            home(bank)
          case 6:
           account.transactionsHistory(account.id)
 except ValueError:
     print("invalid option")
     operations(account,bank,senderFullName)

def deposit(account,senderFullName):
  accountType = ""
  try:

    while True:
        
        amount = float(input("Amount: "))
        userAccountTypeInput = int(input("To:    1- Checking Account     2- Savings Account \n"))

        match userAccountTypeInput:
           case 1:
             accountType = "checking"
             break
           case 2: 
            accountType = "saving"
            break
    transaction = account.deposit(accountType,amount,senderFullName)
 
  except ValueError :
    print("Invalid input")
    deposit(account,senderFullName)
  except InvalidAmountException as excp:
    deposit(account,senderFullName)
    print(excp)
  else: 
   print(transaction)
    
def withdraw(account,senderFullName):
   try:

    while True:
   
        amount = float(input("Amount: "))
        userAccountTypeInput = int(input("From:    1- Checking Account     2- Savings Account \n"))

        match userAccountTypeInput:
           case 1:
             accountType = "checking"
             break
           case 2: 
            accountType = "saving"
            break
    transaction = account.withdraw(accountType,amount,senderFullName)
   except ValueError :
    print("Invalid input")
    withdraw(account,senderFullName)
   except AccountDeactivated as excp:
    print(excp)
   except NotEnoughMoneyException as excp:
    print(excp)
    return
   else: 
    print(transaction)
    

def transfer(account,senderFullName):
 state = False  
 try:
    
    while state == False:  
    
       
       amount = float(input("Amount: "))
       senderAccountTypeInput = int(input("To:    1- Checking Account     2- Savings Account \n"))

       match senderAccountTypeInput:
           case 1:
             accountType = "saving"
             break
           case 2: 
            accountType = "checking"
            break
    transaction = account.transferToDifferentAccountType(accountType,amount,senderFullName)    

 except ValueError :
    print("Invalid input")
    transfer(account,senderFullName)
 except NotEnoughMoneyException as excp :
    print(excp)
    return
 except InvalidAmountException as excp :
    print(excp)
    transfer(account,senderFullName)
 except AccountDeactivated as excp:
    print(excp)   
    return
 else: 
   print(transaction)

def transferToAnotherCustomer(account,bank,senderFullName):
   
   try:
    
    while True:  
    
       
       amount = float(input("Amount: "))
       senderAccountTypeInput = int(input("From:    1- Checking Account     2- Savings Account \n"))
       recipientID = input("ID of recipient")

       match senderAccountTypeInput:
           case 1:
             accountType = "checking"
             break
           case 2: 
            accountType = "saving"
            break
         
    transaction = bank.transferToAnotherCustomer(senderFullName,account,accountType,amount,recipientID)
     
   except ValueError :
    print("Invalid input")
    transferToAnotherCustomer(account,bank,senderFullName)
   except NotEnoughMoneyException as excp :
    print(excp)
    return
   except CustomerNotfoundException as excp:
    print(excp)
    transferToAnotherCustomer(account,bank,senderFullName)
   except AccountDeactivated as excp:
    print(excp)
    return
   else:
    print(transaction)

# LOADING DATA FORM CSV FILE

myBank = Bank()
myBank.loadData()
 
home(myBank)

    
          
        





  

         






