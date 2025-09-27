
import csv
import re
from banking.transaction import Transaction
class NotEnoughMoneyException(Exception):
     pass
class PasswordTooWeak(Exception):
     pass
class AccountDeactivated(Exception):
     pass
class InvalidAmountException(Exception):
     pass
class ImproperPassword(Exception):
    pass
class Account:
     
     def __init__ (self, password ,balanceChecking = 0 ,balanceSavings = 0 ):
        self.id = None
        self.password = self.qualifyPassword(password)
        self.balanceChecking = balanceChecking
        self.balanceSavings = balanceSavings
        self.checkingDeactivated = False
        self.savingsDeactivated = False
        self.checkingDraftCount = 0
        self.savingDraftCount = 0


     def qualifyPassword(self,password):
         if len(password) > 32:
             raise ImproperPassword("Too long password make sure it doesn't exceed 32 characters long")    
         letters = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]"
         if len(str(password)) > 8 and bool(re.search(letters,password)) == True and bool(re.search(r"[qwertyuioplkjghfdsazxcvbnm]",password)) == True and bool(re.search(r"[1234567890]",password)):
            return password
         
         else:      
           raise PasswordTooWeak("Password too weak, password must conatain a character, a digit and one complex character at least") 
         

     
     def deposit(self,accountType,amount,senderName):
           if amount is None or not isinstance(amount,(int,float)) or amount <= 0: 
                raise InvalidAmountException("invalid amount")
            
           if accountType.lower() == "checking":
                self.balanceChecking += amount 
                if self.balanceChecking >= 0:
                    self.checkingDeactivated = False
                    self.checkingDraftCount = 0
                transaction = Transaction("deposit","checking",amount,self.balanceChecking,senderName)
                self.updateTransactionsHistory(self.id,transaction)
                return transaction
           elif accountType.lower() == "saving":
              self.balanceSavings += amount
              if self.balanceSavings >= 0:
                  self.savingsDeactivated = False
                  self.savingDraftCount = 0
              transaction = Transaction("deposit","saving",amount,self.balanceSavings,senderName)
              self.updateTransactionsHistory(self.id, transaction)
              return transaction
           else:        
              raise ValueError("invalid account type")
    
     
     
     
     def withdraw(self,accountType,amount,sender):
        
        if amount is None or not isinstance(amount,(int,float)) : 
                raise InvalidAmountException("invalid amount")
        
        if self.checkAccount(accountType,amount) == True:
         
            if accountType.lower() == "checking":
               if self.checkingDeactivated == True:
                  raise AccountDeactivated("failed Your account is deactivated ")
               if self.balanceChecking - amount < 0 or self.balanceChecking <= 0:
                 return self.handleOverDraft(accountType,amount,self.balanceChecking,sender)
               self.balanceChecking -= amount
               transaction = Transaction("withdraw","checking",amount, self.balanceChecking,sender)
               self.updateTransactionsHistory(self.id,transaction)
               return transaction
           
            elif accountType.lower() == "saving":
              if self.savingsDeactivated == True:
                raise AccountDeactivated("failed Your account is deactivated ")
              if self.balanceSavings - amount < 0 or self.balanceSavings <= 0:
                return self.handleOverDraft(accountType,amount,self.balanceSavings,sender)
            self.balanceSavings -= amount
            transaction = Transaction("withdraw","savings",amount, self.balanceSavings,sender)
            self.updateTransactionsHistory(self.id,transaction)
            return transaction
    

     def transferToDifferentAccountType(self,accountType,transferAmount,sender):
      
      if transferAmount is None or not isinstance(transferAmount,(int,float)) or transferAmount <= 0: 
                raise InvalidAmountException("invalid amount")
      if accountType.lower() == "checking" and self.balanceChecking < transferAmount:
        raise NotEnoughMoneyException("Not enough money in checking account")
      elif accountType.lower() == "saving" and self.balanceSavings < transferAmount:
        raise NotEnoughMoneyException("Not enough money in savings account")
      
      if self.checkAccount(accountType,transferAmount) == True:
          if accountType.lower() == "checking":
              if self.checkingDeactivated == True:
                  raise AccountDeactivated("failed Your account is deactivated ")
              self.balanceChecking -= transferAmount
              self.balanceSavings += transferAmount
              transaction = Transaction("transfer","checking",transferAmount,self.balanceChecking, sender ,"savings" )
              self.updateTransactionsHistory(self.id,transaction)
              return transaction
          else:
              if self.savingsDeactivated == True:
                  raise AccountDeactivated("failed Your account is deactivated ")                     
              self.balanceSavings -= transferAmount
              self.balanceChecking += transferAmount
              transaction = Transaction("transfer","saving",transferAmount,self.balanceSavings, sender, "checking")
              self.updateTransactionsHistory(self.id,transaction)
              return transaction
          
    
    
     def checkAccount(self,accountType,transferAmount):
        balance = None
        if accountType.lower() == "checking":  
            balance = self.balanceChecking

        elif accountType.lower() == "saving":
            balance = self.balanceSavings
        else:
           raise ValueError("invaild account")
        if balance < 0 and transferAmount > 100:
            raise NotEnoughMoneyException("invalid operaion")
        else:
            return True

     
     
     def handleOverDraft(self, accountType, transferAmount,balance,sender):
      if balance - transferAmount < 0:
            if balance - transferAmount -35 >= -100:

               if accountType.lower() == "checking":
                  self.balanceChecking -= transferAmount
                  self.balanceChecking -= 35
                  self.checkingDraftCount += 1
                  if self.checkingDraftCount >= 2:
                      self.checkingDeactivated = True
                  transaction = Transaction("transfer","checking",transferAmount,self.balanceChecking, sender ,"savings" )
                  self.updateTransactionsHistory(self.id,transaction)
                  return transaction
               elif accountType.lower() == "saving":
                    self.balanceSavings -= transferAmount
                    self.balanceSavings -= 35 
                    self.savingDraftCount +=1
                    if self.savingDraftCount >= 2:
                        self.savingsDeactivated = True  
                    tranaction = Transaction("transfer","saving",transferAmount,self.balanceSavings, sender, "checking")
                    self.updateTransactionsHistory(self.id,tranaction)
                    return tranaction
            else:
               if accountType.lower() == "checking":
                  self.checkingDraftCount +=1
                  if self.checkingDraftCount >= 2:
                        self.checkingDeactivated = True  
               else:
                   self.savingDraftCount += 1 
                   if self.savingDraftCount >= 2:
                        self.savingsDeactivated = True  
               raise NotEnoughMoneyException("operation failed your account's balance can't have less than -100$")  




     def updateTransactionsHistory(self,id,trnasaction):
      try:
         with open ("banking/transactions.csv","a", newline= '') as file:
           writer = csv.writer(file)
           transactionList = [id , str(trnasaction)]
           writer.writerow(transactionList)
           
      except Exception:
          print("File can't be written")



     def transactionsHistory(self,accountid):
          transactions = []
          try:
              with open("banking/transactions.csv",'r', newline = "") as file:
                  reader = csv.reader(file)
                  for row in reader:
                      id, transaction = row
                      if str(id) == str(accountid):
                          transactions.append(transaction)
          except Exception:
              print("File cannot be read")                
          for trans in  transactions:
              print(trans)

     def setID(self,id):
        self.id = id


