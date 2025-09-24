
import csv
from banking.account import NotEnoughMoneyException
from banking.account import Account
from banking.customer import Customer
class CustmerAlreadyExist(Exception):
   pass
class CustomerNotfoundException(Exception):
   pass
class Bank:    
  
  customers = []


  def loadData(self):
    with open("banking/bank.csv",'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
        account = Account(row["password"],int (row["balance_checking"]),int(row["balance_savings"]))
        account.setID(int (row["account_id"]))
        customer = Customer(row["frst_name"],row["last_name"],account)
        self.customers.append(customer)
      return self.customers
 


  def addCustomer(self, firstName,lastName,password,checking_amount = 0 ,saving_amount = 0):
    number = int(self.customers[len(self.customers)-1].account.id)
    number +=1
    id = number
    newCustomer = Customer(firstName,lastName,Account(password,checking_amount,saving_amount))
    newCustomer.account.setID(id)
    self.customers.append(newCustomer) 
    return newCustomer

  def transferToDifferentCustomer(self,senderAccount,senderAccountType,transferAmount,recipientID):
         
         if senderAccountType == "checking":
            balance = senderAccount.balanceChecking
         elif senderAccountType == "saving":
            balance = senderAccount.balanceSavings
         else:
           raise ValueError("invaild account")
         if balance < transferAmount:
           raise NotEnoughMoneyException("operation failed you don't have enough money in your account")      
          
         recipientAccount  = self.checkCustomerExists(recipientID)
         if recipientAccount != None:
            if senderAccountType == "checking":
               senderAccount.balanceChecking -= transferAmount
            elif senderAccountType ==  "saving":
               senderAccount.balanceSavings -= transferAmount
            recipientAccount.balanceChecking += transferAmount

  def checkCustomerExists(self,recipientID):
      for customer in self.customers:
          if customer.account.id == recipientID:
            return customer.account
      else:
        raise CustomerNotfoundException(f"There is not custmer with the ID: {recipientID}")
          
 
  def printCustomers(self):
     for cust in self.customers:
      print(cust.account.id,cust.firstName,cust.lastName,cust.account.password,cust.account.balanceChecking,cust.account.balanceSavings)

  

