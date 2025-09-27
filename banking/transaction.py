from datetime import datetime


class Transaction:
  def __init__(self,trans_type,account_type,amount,newBalance,sender,recept = None):
    self.transID = 0
    self.dateNow = datetime.now()
    self.sender = sender
    self.recept = recept
    self.account_type = account_type
    self.trans_type = trans_type
    self.newBalance = newBalance
    self.amount = amount


  def __str__(self):
    if self.trans_type == "deposit":
        return f" {self.dateNow.now()}  {self.trans_type} to {self.account_type}   Amount:  {self.amount}  New Balance: {self.newBalance} | {self.sender}"
    elif self.trans_type == "withdraw":
        return f" {self.dateNow.now()}  {self.trans_type} from {self.account_type}   Amount:  {self.amount}  New Balance: {self.newBalance} {self.sender} "
    elif self.trans_type == "transfer":
       return f" {self.dateNow.now()}  {self.trans_type}  {self.account_type}   Amount:  {self.amount}  New Balance: {self.newBalance} from {self.sender} to: {self.recept} "
