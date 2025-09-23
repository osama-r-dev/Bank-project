

import unittest
from Bank.account import InvalidCharacterException
from Bank.account import NameTooLongException
from Bank.account import Account

class TestAccount(unittest.TestCase):
  def setUp(self):
           self.account = Account("osama","alrehaili")
     
  
       
          



  def test_name_too_long(self):
      with self.assertRaises(NameTooLongException):
         Account("osamaaaaaaaaaaaa","alrehaili") # osama..a contains more than 15 chars shouold fail
           

  def test_invalid_character(self):
      with self.assertRaises(InvalidCharacterException):    # testing invalid characters for the first and last names of the account
        Account("osma","alrehaili") 
        Account("11","alrehaili")  
        Account("osa@r(ma","alrehaili")

  def test_name_is_valid(self):
        
        self.assertEqual(self.account.qualifyName(self.account.firstName),"osama")
        self.assertEqual(self.account.qualifyName(self.account.lastname),"alrehaili")
         
  

           


 
           
           


 
