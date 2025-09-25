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
   except InvalidAcountInfo:
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
         
     operations(account)    

## working on this so far
def operations(account):
 try:
     userInput = int(input("1- My accounts    2- deposit   3- withdraw  4- transfer \n"))
     match userInput:
          case 1:
           print(f" Checking Account => Balance: {account.balanceChecking}/n")    
          case 2:
             pass 
          case 3: 
              pass
 except ValueError:
     pass


# LOADING DATA FORM CSV FILE

exit = False
myBank = Bank()
myBank.loadData()
firstName = ''
lastName = ''
password = ''
 
while exit != True:
   home(myBank)

    
          
        





  

         






