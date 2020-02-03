def get_full_name(first,last,middle=""):
	if middle:
		full_name = '{0} {1} {2}'.format(first,middle,last)
	else:
		full_name = '{0} {1}'.format(first,last)
	return full_name.title()
class Accountant():
	def __init__(self,balance=0):
		self.balance=balance
	def deposit(self,amount):
		self.balance+=amount
	def withdraw(self,amount):
		self.balance-=amount