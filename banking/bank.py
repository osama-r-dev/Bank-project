
import csv
from banking.account import NotEnoughMoneyException
from banking.account import Account
from banking.customer import Customer
class CustmerAlreadyExist(Exception):
   pass
class CustomerNotfoundException(Exception):
   pass
class InvalidAcountInfo(Exception):
   pass
class Bank:    

  def __init__(self):
   self.customers = []

  def loadData(self):
    with open("banking/bank.csv",'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
        account = Account(row["password"],float (row["balance_checking"]),float(row["balance_savings"]))
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

  def transferToAnotherCustomer(self,senderAccount,senderAccountType,transferAmount,recipientID):
         if transferAmount is None or not isinstance(transferAmount,(int,float)) or transferAmount <= 0: 
                raise ValueError("invalid amount")
         if senderAccountType == "checking":
            balance = senderAccount.balanceChecking
         elif senderAccountType == "saving":
            balance = senderAccount.balanceSavings
         else:
           raise ValueError("invaild account type")
         if balance < transferAmount:
           raise NotEnoughMoneyException("operation failed you don't have enough money in your account")      
          
         recipientCustomer= self.checkCustomerExists(recipientID)
         recipientAccount = recipientCustomer.account
         if recipientAccount != None:
            if senderAccountType == "checking":
               senderAccount.balanceChecking -= transferAmount
               recipientAccount.balanceChecking += transferAmount
               return [senderAccount.balanceChecking,recipientCustomer]
            elif senderAccountType ==  "saving":
               senderAccount.balanceSavings -= transferAmount
               recipientAccount.balanceChecking += transferAmount
               return [senderAccount.balanceSavings,recipientCustomer]

  def checkCustomerExists(self,recipientID):
      if recipientID.isdigit() == False:
        raise ValueError("invalid user")
      recipientID = int(recipientID)
      for customer in self.customers:
          if customer.account.id == recipientID:
            return customer
      else:
        raise CustomerNotfoundException(f"There is no custmer with the ID: {recipientID}")

  def login(self, customerID , password):      
      if customerID.isdigit() == False:
        raise ValueError("invalid user")
      customerID = int(customerID)
      for customer in self.customers:
         customerAccount = customer.account
         if customerAccount.id == customerID and customerAccount.password == password:
            return customerAccount
         
      else:
          raise InvalidAcountInfo("Wrong username/password")   
                   
 
  def printCustomers(self):
     for cust in self.customers:
      print(cust.account.id,cust.firstName,cust.lastName,cust.account.password,cust.account.balanceChecking,cust.account.balanceSavings)

  

