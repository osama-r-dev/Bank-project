

import unittest
from banking.customer import Customer
from banking.customer import InvalidCharacterException
from banking.customer import NameTooLongException


class TestAccount(unittest.TestCase):
  def setUp(self):
     self.customer = Customer("osama","alrehaili")
     
  
       
          



  def test_name_too_long(self):
      with self.assertRaises(NameTooLongException):
         Customer("osamaaaaaaaaaaaaa","alrehaili") # osama..a contains more than 15 chars shouold fail
           

  def test_invalid_character(self):
      with self.assertRaises(InvalidCharacterException):    # testing invalid characters for the first and last names of the cusotmer
        Customer("osam3a","alrehaili") 
        Customer("ee3","alrehaili")  
        Customer("osa@r(ma","alrehaili")

  def test_name_is_valid(self):
        
        self.assertEqual(self.customer.qualifyName(self.customer.firstName),"osama")
        self.assertEqual(self.customer.qualifyName(self.customer.lastname),"alrehaili")
         
  

         


 
           
           


 
