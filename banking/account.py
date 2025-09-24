

class NotEnoughMoneyException(Exception):
   pass
class PasswordTooShort(Exception):
     pass

class Account:
     number = 0
    
     def __init__ (self,id, password ,balanceChecking = None ,balanceSavings = None ):
        self.id = id
        self.password = self.qualifyPassword(password)
        self.balanceChecking = balanceChecking
        self.balanceSavings = balanceSavings

     def qualifyPassword(self,password):
        if len(password) < 8:
         raise PasswordTooShort("Too short password") 
        else:      
         return password
      

     def deposit(self,accountType,amount):
        if accountType == "checking":
           self.balanceChecking += amount
        elif accountType == "saving":
           self.balanceSavings += amount
        else:
           raise ValueError("invalid account")
        
     def withdraw(self,accountType,amount):
        if accountType == "checking":
           balance = self.balanceChecking
        elif accountType == "saving":
            balance = self.balanceSavings
        else:
           raise ValueError("invaild account")
        if balance < amount:
           raise NotEnoughMoneyException("opration failed you don't have enough maoney in your account")
        else:
           if accountType == "checking":
            self.balanceChecking -= amount
            return True
           else:
              self.balanceSavings -= amount
              return True


     def transferToDifferentAccountType(self,accountType,transferAmount):
          if accountType == "checking":
               balance = self.balanceChecking
          elif accountType == "saving":
               balance = self.balanceSavings
          else:
               raise ValueError("invaild account")
          if balance < transferAmount:
             raise NotEnoughMoneyException("operation failed you don't have enough money in your account")
          if accountType == "checking":
             self.balanceChecking -= transferAmount
             self.balanceSavings += transferAmount
          else:
             self.balanceSavings -= transferAmount
             self.balanceChecking += transferAmount
             return True
     def transferToDifferentCustomer(customerAccountType,trnasferAmount):
        pass

def checkingAccount():
    pass

def savingAccount():
    pass

