

class NotEnoughMoneyException(Exception):
   pass
class PasswordTooShort(Exception):
     pass
class AccountDeactivated(Exception):
    pass
class InvalidAmountException(Exception):
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
        if len(str(password)) < 8:
         raise PasswordTooShort("Too short password") 
        else:      
         return password
      

     def deposit(self,accountType,amount):
           if amount is None or not isinstance(amount,(int,float)) or amount <= 0: 
                raise InvalidAmountException("invalid amount")
            
           if accountType.lower() == "checking":
                self.balanceChecking += amount 
                if self.balanceChecking >= 0:
                    self.checkingDeactivated = False
                    self.checkingDraftCount = 0
                return self.balanceChecking
           elif accountType.lower() == "saving":
              self.balanceSavings += amount
              if self.balanceSavings >= 0:
                  self.savingsDeactivated = False
                  self.savingDraftCount = 0
              return self.balanceSavings
           else:        
              raise ValueError("invalid account type")
    
     def withdraw(self,accountType,amount):
        
        if amount is None or not isinstance(amount,(int,float)) : 
                raise InvalidAmountException("invalid amount")
        
        if self.checkAccount(accountType,amount) == True:
         
            if accountType.lower() == "checking":
               if self.checkingDeactivated == True:
                  raise AccountDeactivated("failed Your account is deactivated ")
               if self.balanceChecking - amount < 0 or self.balanceChecking <= 0:
                 return self.handleOverDraft(accountType,amount,self.balanceChecking)
               self.balanceChecking -= amount
               return self.balanceChecking
           
            elif accountType.lower() == "saving":
              if self.savingsDeactivated == True:
                raise AccountDeactivated("failed Your account is deactivated ")
              if self.balanceSavings - amount < 0 or self.balanceSavings < 0:
                return self.handleOverDraft(accountType,amount,self.balanceSavings)
            self.balanceSavings -= amount
            return self.balanceSavings

     def transferToDifferentAccountType(self,accountType,transferAmount):

      if transferAmount is None or not isinstance(transferAmount,(int,float)) or transferAmount <= 0: 
                raise InvalidAmountException("invalid amount")
      if self.checkAccount(accountType,transferAmount) == True:
          if accountType.lower() == "checking":
              if self.checkingDeactivated == True:
                  raise AccountDeactivated("failed Your account is deactivated ")
              self.balanceChecking -= transferAmount
              self.balanceSavings += transferAmount
            
          else:
              if self.savingsDeactivated == True:
                  raise AccountDeactivated("failed Your account is deactivated ")                     
              self.balanceSavings -= transferAmount
              self.balanceChecking += transferAmount

      return [self.balanceChecking,self.balanceSavings]
          

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

     def handleOverDraft(self, accountType, transferAmount,balance):
      if balance - transferAmount < 0:
            if balance - transferAmount -35 >= -100:

               if accountType.lower() == "checking":
                  self.balanceChecking -= transferAmount
                  self.balanceChecking -= 35
                  self.checkingDraftCount += 1
                  if self.checkingDraftCount >= 2:
                      self.checkingDeactivated = True
                  return self.balanceChecking
               elif accountType.lower() == "saving":
                    self.balanceChecking -= transferAmount
                    self.balanceSavings -= 35 
                    self.savingDraftCount +=1
                    if self.savingDraftCount >= 2:
                        self.savingsDeactivated = True  
                    return self.balanceSavings
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


     def setID(self,id):
        self.id = id

def checkingAccount():
    pass

def savingAccount():
    pass

