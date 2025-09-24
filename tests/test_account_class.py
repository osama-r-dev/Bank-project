
import unittest

from banking.account import Account
from banking.account import NotEnoughMoneyException
from banking.account import PasswordTooShort
class TestAccountClass(unittest.TestCase):
    account = Account("12345678",1000,1000)
    
    
    def test_password(self):
        with self.assertRaises(PasswordTooShort): 
            Account("1234567",10000,100)
    
    
    def test_deposit_passing_random_value(self):
       with self.assertRaises(ValueError):
           self.account.deposit("nothing",100)

    
    def test_withdraw_with_not_enough_money(self):
        with self.assertRaises(NotEnoughMoneyException):   
            self.account.withdraw("checking",10000)

    def test_deposit_operation(self):
        self.assertEqual(self.account.deposit("checking",1000),2000)
        self.assertEqual(self.account.deposit("checking",1000),3000)

    
    def test_withdraw_operation(self):
        self.assertEqual(self.account.withdraw("checking",1000),200)
            