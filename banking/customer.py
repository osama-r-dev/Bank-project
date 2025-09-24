
class NameTooLongException(Exception):
     pass
class InvalidCharacterException(Exception):
     pass


class Customer:
     
     def __init__ (self,firstName,lastName,account):

        self.firstName = self.qualifyName(firstName)
        self.lastName =  self.qualifyName(lastName)
        self.account = account
       

     def qualifyName(self,name):
        
           validChars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_")
           if len(name) > 15:    #This is based on Alrajhy bank in saudi
              raise NameTooLongException("The name you entered must contain 15 at mixmum")
            
           else:
              nameChars = list(name)
              for char in nameChars:
                   if char in validChars:
                        continue
                   else:
                        raise InvalidCharacterException("Valid characters are only (a-z), (A-Z), _")
           return name
    
     
       
                 
 
     