from banking.bank import Bank
from banking.account import Account
from banking.account import PasswordTooShort
from banking.customer import Customer
from banking.customer import NameTooLongException
from banking.bank import InvalidAcountInfo
from banking.customer import InvalidCharacterException
from banking.account import InvalidAmountException
from banking.account import AccountDeactivated
from banking.account import NotEnoughMoneyException
from banking.bank import CustomerNotfoundException

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
            withdraw(account)
          case 4:
           option = int(input("1- between my accounts   2- to a customer"))
           match option:
              case 1:
                 transfer(account)
                 
              case 2:
                 transferToAnotherCustomer(account,bank)
                 
          case 5:
            home(bank)
 except ValueError:
     print("invalid option")
     operations(account,bank)

def deposit(account):
  state = False
  accountType = ""
  newBalance = 0
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
    newBalance = account.deposit(accountType,amount)
 
  except ValueError :
    print("Invalid input")
    deposit(account)
  except InvalidAmountException as excp:
    deposit(account)
    print(excp)
  else: 
    print(f"""
 Succuess Deposit of:   {amount}
 New Balance:   {newBalance}         
 """)
    
def withdraw(account):
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
    newBalance = account.withdraw(accountType,amount)
   except ValueError :
    print("Invalid input")
    withdraw(account)
   except AccountDeactivated as excp:
    print(excp)
   except NotEnoughMoneyException as excp:
    print(excp)
    return
   else: 
    print(f"""
 Succuess withdraw of:   {amount}
 New Balance:   {newBalance}         
 """)
    

def transfer(account):
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
    newBalance = account.transferToDifferentAccountType(accountType,amount)    

 except ValueError :
    print("Invalid input")
    transfer(account)
 except NotEnoughMoneyException as excp :
    print(excp)
    return
 except InvalidAmountException as excp :
    print(excp)
    transfer(account)
 except AccountDeactivated as excp:
    print(excp)   
    return
 else: 
    print(f"""
 Succuess withdraw of:   {amount}
 New Balance:   {newBalance}         
 """)

def transferToAnotherCustomer(account,bank):
   
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
         
    transferResult = bank.transferToAnotherCustomer(account,accountType,amount,recipientID)
    recipientFirstName = transferResult[1].firstName
    recipientLastName = transferResult[1].lastName 
    newBalance = transferResult[0]
     
   except ValueError :
    print("Invalid input")
    transferToAnotherCustomer(account,bank)
   except NotEnoughMoneyException as excp :
    print(excp)
    return
    transferToAnotherCustomer(account,bank)
   except CustomerNotfoundException as excp:
    print(excp)
    transferToAnotherCustomer(account,bank)
   except AccountDeactivated as excp:
    print(excp)
    return
   else:
    print(f"""
    Succuess of transfer:   {amount}
    To:  {recipientFirstName} {recipientLastName}        
    New Balance:   {newBalance} 
    """)





# LOADING DATA FORM CSV FILE

exit = False
myBank = Bank()
myBank.loadData()
firstName = ''
lastName = ''
password = ''
 
while exit != True:
   home(myBank)

    
          
        





  

         






