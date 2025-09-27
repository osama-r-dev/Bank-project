
import unittest

from banking.account import Account
from banking.account import NotEnoughMoneyException
from banking.account import AccountDeactivated
from banking.account import PasswordTooWeak
from banking.account import InvalidAmountException
class TestAccountClass(unittest.TestCase):
    account1 = Account("1234df$5678",1000,1000)
    account2 = Account("1234567fd$890",3,1000)
    account3 = Account("123456fg@781",0,3000)
    account4 =  Account("fdfafd3@sfad",0,1000)
    account5 =  Account("fdf4$afdsfad",0,100)
    account6 =  Account("fdfafds1@fad",0,100)
    def test_password(self):
        with self.assertRaises(PasswordTooWeak): 
            Account("1267",10000,100)
    
    def test_deposit_passing_random_value(self):
       with self.assertRaises(InvalidAmountException):
           self.account1.deposit("nothing",-100,"osama")
           self.account2.deposit("checking","d","osama")
           self.account2.deposit("checking",-1000,"osama") 
           self.account2.deposit("checking", 0,"osama") 
    
    
    def test_withdraw_overdraft(self):   
           self.assertEqual(self.account3.withdraw("checking",30,"osama").newBalance,-65)

    def test_withdraw_with_not_enough_money(self):
        with self.assertRaises(NotEnoughMoneyException):   
           #self.account4.withdraw("checking",101)
             self.account6.withdraw("checking",66,"ME")
            #  self.account5.withdraw("checking",10)
 
    def test_account_deactivation(self):
           with self.assertRaises(AccountDeactivated):
             self.account5.withdraw("checking",20,"osama")
             self.account5.withdraw("checking",9,"osama")
             self.account5.withdraw("checking",1,"osama")
              

    def test_deposit_operation(self):
        self.assertEqual(self.account1.deposit("checking",1000,"osama").newBalance,2000)
        self.assertEqual(self.account1.deposit("checking",1000,"osama").newBalance,3000)
        

    
    # def test_withdraw_operation(self):
    #     self.assertEqual(self.account1.withdraw("checking",1000,"osama").newBalance,2000)


    # def test_transfer_to_different_accountType(self):
    #     self.assertEqual(self.account3.transferToDifferentAccountType("checking",1000),[5000,4000])   
    #     self.assertEqual(self.account3.transferToDifferentAccountType("saving",4000),[9000,0])     


    