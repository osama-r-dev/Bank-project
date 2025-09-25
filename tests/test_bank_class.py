import unittest
from banking.customer import Customer
from banking.bank import Bank
from banking.customer import NameTooLongException
from banking.bank import CustomerNotfoundException


class TestBank(unittest.TestCase):
    def setUp(self):  
     self.bank1 = Bank()
     self.bank1.loadData()  # this loads the first 5 people inside the dsv file so the id is 6 for the next customer
     self.bank1.addCustomer("osama","alrehaili","343434343",1000,2000)
    
     self.bank2 = Bank()
     self.bank2.loadData()
     self.sami = self.bank2.addCustomer("Sami","alrehaili","12345678",1000,4000)
     self.ahmad = self.bank2.addCustomer("ahmad","khaled","1111111111",1000,6000)

    def test_add_customer(self):
      lastCustomer = self.bank1.customers[len(self.bank1.customers)-1]
      self.assertEqual(lastCustomer.account.id ,6)
      self.assertEqual(lastCustomer.firstName ,"osama")
      self.assertEqual(lastCustomer.lastName ,"alrehaili")
      self.assertEqual(lastCustomer.account.password ,"343434343")
      self.assertEqual(lastCustomer.account.balanceChecking ,1000)
      self.assertEqual(lastCustomer.account.balanceSavings ,2000)
         
    def test_transfer_to_another_customer(self):
         ahmadAccoount = self.ahmad.account
         samiAccount = self.sami.account
         self.bank2.transferToDifferentCustomer(ahmadAccoount,"saving",1000,6)
         self.assertEqual(ahmadAccoount.balanceSavings,5000)
         self.assertEqual(samiAccount.balanceChecking,2000)

    def test_transfer_to_wrong_id(self):
          with self.assertRaises(CustomerNotfoundException):
              self.bank2.transferToDifferentCustomer(self.ahmad.account,"checking",1000,100)   
    

    # test amount
    



    #test invalid account type