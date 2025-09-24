 
from banking.bank import Bank

myBank = Bank()
myBank.loadData()

account = myBank.customers[1].account
account.deposit("checking",1000)
account.withdraw("checking",1001)
account.transferToDifferentAccountType("dfdf",1)
myBank.printCustomers()
