
import csv
from banking.account import Account
from banking.customer import Customer
class CustmerAlreadyExist(Exception):
   pass

class Bank:    
 number = 0
 def __init__(self):
  pass
          
        
    
    
def addCustomer(self, firstName,lastName,password,accountType):
        Bank.number +=1
        id ="1000"+ str(Bank.number )
        with open('banking/bank.csv','r') as file:
              reader = csv.DictReader(file)
              for row in reader:
                   if row.get("account_id") == id:
                    raise CustmerAlreadyExist("Customer already exist")
                    
                   else:
                    newCustomer = Customer(firstName,lastName,Account(id,password))
                    StoreData(newCustomer,accountType)


def StoreData(customer, accountType):
   pass
                 
                   

 
      





 