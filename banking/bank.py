
import csv
from banking.account import Account
from banking.customer import Customer
class CustmerAlreadyExist(Exception):
   pass

class Bank:    
  
  customers = []


  def loadData(self):
    with open("banking/bank.csv",'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
        account = Account(row["account_id"],row["password"],int (row["balance_checking"]),int(row["balance_savings"]))
        customer = Customer(row["frst_name"],row["last_name"],account)
        self.customers.append(customer)
      return self.customers
 


  def addCustomer(self, firstName,lastName,password,checking_amount = None ,saving_amount = None):
    number = int(self.customers[len(self.customers)-1].account.id)
    number +=1
    id = number
    newCustomer = Customer(firstName,lastName,Account(id,password,checking_amount))
    self.customers.append(newCustomer) 
    
 
  def printCustomers(self):
     for cust in self.customers:
      print(cust.account.id,cust.firstName,cust.lastName,cust.account.password,cust.account.balanceChecking,cust.account.balanceSavings)



