
import unittest

from banking.account import Account
from banking.account import NotEnoughMoneyException
from banking.account import AccountDeactivated
from banking.account import PasswordTooShort
from banking.account import InvalidAmountException
class TestAccountClass(unittest.TestCase):
    account1 = Account("12345678",1000,1000)
    account2 = Account("1234567890",3,1000)
    account3 = Account("123456781",6000,3000)
    account4 =  Account("fdfafdsfad",0,1000)
    account5 =  Account("fdfafdsfad",0,100)
    account6 =  Account("fdfafdsfad",0,100)
    def test_password(self):
        with self.assertRaises(PasswordTooShort): 
            Account("1267",10000,100)
    
    def test_deposit_passing_random_value(self):
       with self.assertRaises(InvalidAmountException):
           self.account1.deposit("nothing",-100)
           self.account2.deposit("checking","d")
           self.account2.deposit("checking",-1000) 
           self.account2.deposit("checking", 0) 
    
    
    def test_withdraw_with_not_enough_money(self):
        with self.assertRaises(NotEnoughMoneyException):   
           self.account4.withdraw("checking",1000)

    def test_withdraw_with_not_enough_money(self):
        with self.assertRaises(NotEnoughMoneyException):   
           #self.account4.withdraw("checking",101)
             self.account5.withdraw("checking",66)
            #  self.account5.withdraw("checking",10)
 
    def test_account_deactivation(self):
           with self.assertRaises(AccountDeactivated):
             self.account5.transferToDifferentAccountType("checking",20)
             self.account5.transferToDifferentAccountType("checking",10)
              

    def test_deposit_operation(self):
        self.assertEqual(self.account1.deposit("checking",1000),2000)
        self.assertEqual(self.account1.deposit("checking",1000),3000)
        self.assertEqual(self.account6.withdraw("checking",30),-65)

    
    def test_withdraw_operation(self):
        self.assertEqual(self.account1.withdraw("checking",1000),2000)


    def test_transfer_to_different_accountType(self):
        self.assertEqual(self.account3.transferToDifferentAccountType("checking",1000),[5000,4000])   
        self.assertEqual(self.account3.transferToDifferentAccountType("saving",4000),[9000,0])     


    