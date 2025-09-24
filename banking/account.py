

class NotEnoughMoneyException(Exception):
   pass
class PasswordTooShort(Exception):
     pass

class Account:
     
     def __init__ (self, password ,balanceChecking = 0 ,balanceSavings = 0 ):
        self.id = None
        self.password = self.qualifyPassword(password)
        self.balanceChecking = balanceChecking
        self.balanceSavings = balanceSavings
        
     def qualifyPassword(self,password):
        if len(password) < 8:
         raise PasswordTooShort("Too short password") 
        else:      
         return password
      

     def deposit(self,accountType,amount):
           if amount is None or not isinstance(amount,(int,float)) or amount <= 0: 
                raise ValueError("invalid amount")
           if accountType.lower() == "checking":
                self.balanceChecking += amount 
                return self.balanceChecking
           elif accountType.lower() == "saving":
              self.balanceSavings += amount
              return self.balanceSavings
           else:        
              raise ValueError("invalid account")
    
     def withdraw(self,accountType,amount):
        if amount is None or not isinstance(amount,(int,float)) or amount <= 0: 
                raise ValueError("invalid amount")
        if self.checkAccount(accountType,amount) == True:
           if accountType.lower() == "checking":
            self.balanceChecking -= amount
            return self.balanceChecking
           else:
              self.balanceSavings -= amount
              return self.balanceSavings

     def transferToDifferentAccountType(self,accountType,transferAmount):
      if transferAmount is None or not isinstance(transferAmount,(int,float)) or transferAmount <= 0: 
                raise ValueError("invalid amount")
      if self.checkAccount(accountType,transferAmount) == True:
          if accountType.lower() == "checking":
             self.balanceChecking -= transferAmount
             self.balanceSavings += transferAmount
            
          else:                     
             self.balanceSavings -= transferAmount
             self.balanceChecking += transferAmount
      return [self.balanceChecking,self.balanceSavings]
          

     def checkAccount(self,accountType,transferAmount):
        if accountType.lower() == "checking":  
            balance = self.balanceChecking
        elif accountType.lower() == "saving":
            balance = self.balanceSavings
        else:
           raise ValueError("invaild account")
        if balance < transferAmount:
           raise NotEnoughMoneyException("operation failed you don't have enough money in your account")      
        return True


     def setID(self,id):
        self.id = id

def checkingAccount():
    pass

def savingAccount():
    pass

