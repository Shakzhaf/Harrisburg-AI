class CreditCard:

	def __init__(self, customer, bank, account, limit):
		self._customer = customer
		self._bank = bank
		self._account = account
		self._balance = 0.0
		self._limit = limit
		
	def get_customer(self):
		return self._customer
	
	def get_bank(self):
		return self._bank
	
	def get_accimitount(self):
		return self._account
	
	def get_balance(self):
		return self._balance
	
	def get_bank(self):
		return self._limit
	
	def charge(self, price):
		if(price >= 0.0 and price + self._balance <= self._limit):
			self._balance = price + self._balance
			return True
		return False
	
	def make_payment(self, amount):
		if(amount >= 0.0 and amount <= self._balance):
			self._balance = self._balance - amount
			return True
		return False