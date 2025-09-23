


class PasswordTooShort(Exception):
     pass

class Account:
     number = 0
    
     def __init__ (self,id, password):
        self.id = id
        self.password = self.qualifyPassword(password)
        self.balanceChecking = None
        self.savingsAccount = None

   


class SavingsAccount(Account):
        def __init__( self, firstName,lastName,password):
            super().__init__(id, firstName, lastName,password)
           

 
def qualifyPassword(self,password):
        if len(password) < 8:
         raise PasswordTooShort("Too short password") 
        else:      
         return password
      
def setCheckingAccount():
    pass

def setSavingAccount():
    pass