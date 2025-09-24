import unittest
from banking.customer import Customer
from banking.bank import Bank
from banking.customer import NameTooLongException



class TestBank(unittest.TestCase):
    def setUp(self):  
     self.bank = Bank()
     self.bank.loadData()  # this loads the first 5 people inside the dsv file so the id is 6 for the next customer
     self.bank.addCustomer("osama","alrehaili","343434343",1000,0)
     

    
    def test_add_customer(self):
      lastCustomer = self.bank.customers[len(self.bank.customers)-1]
      self.assertEqual(lastCustomer.account.id ,6)
      self.assertEqual(lastCustomer.firstName ,"osama")
      self.assertEqual(lastCustomer.lastName ,"alrehaili")
      self.assertEqual(lastCustomer.account.password ,"343434343")
      self.assertEqual(lastCustomer.account.balanceChecking ,1000)
      self.assertEqual(lastCustomer.account.balanceSavings ,0)
         
        