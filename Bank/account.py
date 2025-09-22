

class NameTooLongException(Exception):
     pass
class InvalidCharacterException(Exception):
     pass
class TooWeakPassword(Exception):
     pass

class Account:
    def __init__ (self,id, firstName,lastName, password, balanceChecking ):
        self.id = id
        QualifyName(firstName)
        QualifyName(lastName)

        self.firstName = firstName
        self.lastname = lastName
        self.password = password
        self.balanceChecking = balanceChecking
        

    def qualifyName(name):
         validChars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_")
         if len(name) > 15:    #This is based on Alrajhy bank in saudi
            raise NameTooLongException("The name you entered must contain 15 at mixmum")
         else:
            nameChars = name.split("")
            for char in nameChars:
                 if char in validChars:
                      continue
                 else:
                      raise InvalidCharacterException("Valid characters are only (a-z), (A-Z), _")
    def qualifyPassword(passaword):
        pass         

class SavingsAccount(Account):
        def __init__( self, id, firstName,lastName, password, balanceSavings ):
            super().__init__(id, firstName, lastName, password, balanceSavings)
            self.balanceSavings = balanceSavings




        
        