from CreditCard import CreditCard

class ChippedCreditCard(CreditCard):

	def __init__(self, customer, bank, account, limit, ccv, chip_type):
		super().__init__(customer, bank, account, limit)
		self._ccv = ccv
		self._chip_type = chip_type
	
	def get_ccv(self):
		return self._ccv
	
	def get_chip_type(self):
		return self._chip_type