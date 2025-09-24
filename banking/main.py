 
from banking.bank import Bank

myBank = Bank()
myBank.loadData()

account_suresh = myBank.customers[0].account
account_james = myBank.customers[1].account
 
myBank.transferToDifferentCustomer(account_suresh,"checking",1000,2)
myBank.printCustomers()

