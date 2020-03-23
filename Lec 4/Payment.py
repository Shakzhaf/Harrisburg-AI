from abc import ABC, abstractmethod

class Payment(ABC):

	def __init__(self, type, amount):
		self._type = type
		self._amount = amount
	
	def get_type(self):
		return self._type
	
	def get_amount(self):
		return self._amount
	
	@abstractmethod
	def payment(self):
		pass