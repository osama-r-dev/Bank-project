from banking.bank import Bank
from banking.account import Account
from banking.account import PasswordTooShort
from banking.customer import Customer
from banking.customer import NameTooLongException
from banking.bank import InvalidAcountInfo
from banking.customer import InvalidCharacterException
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
             pass   
          case 4:
              bank.printCustomers()    
   except ValueError:
     print("invalid option")           

def createNewAccount(bank):
    state = False
    while state == False:
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

        except PasswordTooShort as excp:
            print(excp)   

        else:
         print("customer has been added")   
         state = True
       

def login(bank):
     account = None
     while account == None:
        try: 
             userID = input("user name: ")
             userPassword = (input("password: "))
             account = bank.login(userID,userPassword)

        except InvalidAcountInfo as e:
            print(e)
        except ValueError as e:
            print(e)

        else:    
            
         print("Success")    
         
     operations(account,bank)    

## working on this so far
def operations(account,bank):
 try:
  while True:
     userInput = int(input("1- My accounts    2- Deposit   3- Withdraw  4- Transfer  -5 Home \n"))
     match userInput:
          case 1:
               while True:
                try:
                 print(f""" Checking Account => Balance: {account.balanceChecking} | Savings Account => Balance: {account.balanceSavings}     1- Back""") 
                 option = int(input(""))
                 if option == 1:
                   operations(account,bank)
                   break
                except ValueError:
                  print("Invalid option")
          case 2:
            deposit(account) 
          case 3: 
            break
          case 4:
           break
          case 5:
            break
            home(bank)
 except ValueError:
     print("invalid option")
     operations(account,bank)

def deposit(account):
 state = False
 accountType = ""
 try:
    while True:
   
        userAccountTypeInput = input("To:    1- Checking Account 2- Savings Account")
        amount = input("Amount")

        match userAccountTypeInput:
           case 1:
             accountType = "checking"
             account.deposit(accountType,amount)
             break
           case 2: 
            accountType = "saving"
            break
    account.deposit(accountType,amount)
 
 except ValueError as excp:
    print(excp)
    print("success")
















# LOADING DATA FORM CSV FILE

exit = False
myBank = Bank()
myBank.loadData()
firstName = ''
lastName = ''
password = ''
 
while exit != True:
   home(myBank)

    
          
        





  

         






