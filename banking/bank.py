
import csv
from banking.transaction import Transaction
from banking.account import NotEnoughMoneyException
from banking.account import Account
from banking.account import AccountDeactivated
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
    number = 0
    if len(self.customers) != 0:
       number = int(self.customers[len(self.customers)-1].account.id)
    number +=1
    id = int(number)
    newCustomer = Customer(firstName,lastName,Account(password,checking_amount,saving_amount))
    newCustomer.account.setID(id)
    self.customers.append(newCustomer) 
    return newCustomer



  def transferToAnotherCustomer(self,customerName,senderAccount,senderAccountType,transferAmount,recipientID):
         if transferAmount is None or not isinstance(transferAmount,(int,float)) or transferAmount <= 0: 
                raise ValueError("invalid amount")
         if senderAccountType == "checking":
             if senderAccount.checkingDeactivated == True:
               raise AccountDeactivated("failed Your account is deactivated ")
             balance = senderAccount.balanceChecking
         elif senderAccountType == "saving":
             if senderAccount.checkingDeactivated == True:
                raise AccountDeactivated("failed Your account is deactivated ")
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
               transaction = Transaction("transfer",senderAccountType,transferAmount, senderAccount.balanceChecking,customerName ,recipientCustomer.firstName +" "+ recipientCustomer.lastName)
               senderAccount.updateTransactionsHistory(senderAccount.id,transaction)
               return transaction
            elif senderAccountType ==  "saving":
               senderAccount.balanceSavings -= transferAmount
               recipientAccount.balanceChecking += transferAmount
               transaction =  Transaction("transfer",senderAccountType,transferAmount, senderAccount.balanceChecking,customerName ,recipientCustomer.firstName + " "+ recipientCustomer.lastName)
               senderAccount.updateTransactionsHistory(senderAccount.id,transaction)
               return transaction
  
  
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
            return customer
         
      else:
          raise InvalidAcountInfo("Wrong username/password")   
                   
 
  def printCustomers(self):
     for cust in self.customers:
      print(cust.account.id,cust.firstName,cust.lastName,cust.account.password,cust.account.balanceChecking,cust.account.balanceSavings)

  

  def updateData(self):
     with open("banking/bank.csv","w",newline="") as file:
        listValues = ["account_id","frst_name","last_name","password","balance_checking","balance_savings"]
        writer = csv.DictWriter(file , fieldnames = listValues)
        writer.writeheader()
        for customer in self.customers:
          dic = {
           "account_id": customer.account.id,
            "frst_name": customer.firstName,
             "last_name": customer.lastName,
              "password": customer.account.password,
               "balance_checking": customer.account.balanceChecking,
                 "balance_savings": customer.account.balanceSavings,
           
          }
          writer.writerow(dic)