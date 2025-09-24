import unittest
from banking.customer import Customer
from banking.customer import Bank
from banking.customer import NameTooLongException



class TestBank(unittest.TestCase):
    def setUp(self):
     bank = Bank()

    
    def test_add_customer(self):
        
        self.assertEqual()