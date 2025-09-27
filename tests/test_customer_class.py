

import unittest
from banking.customer import Customer
from banking.customer import InvalidCharacterException
from banking.customer import NameTooLongException
from banking.account import Account


class TestAccount(unittest.TestCase):
  def setUp(self):
     self.account = Account("sdfsdf33#dd ",0,0)
     self.customer = Customer("osama","alrehaili",self.account)
  
  def test_name_too_long(self):
      with self.assertRaises(NameTooLongException):
         Customer("osamaaaaaaaaaaaaa","alrehaili",self.account) # osama..a contains more than 15 chars shouold fail
           

  def test_invalid_character(self):
      with self.assertRaises(InvalidCharacterException):    # testing invalid characters for the first and last names of the cusotmer
        Customer("osam3a","alrehaili",self.account) 
        Customer("ee3","alrehaili",self.account)  
        Customer("osa@r(ma","alrehaili",self.account)

  def test_name_is_valid(self):
        
        self.assertEqual(self.customer.qualifyName(self.customer.firstName),"osama")
        self.assertEqual(self.customer.qualifyName(self.customer.lastName),"alrehaili")
         
  

         


 
           
           


 
