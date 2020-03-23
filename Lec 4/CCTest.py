from CreditCard import CreditCard

c1 = CreditCard("Brian", "The Bank", 12345, 7)
print(c1.get_customer())
c1.charge(1.5)
print(c1.get_balance())
c1.make_payment(.6)
print(c1.get_balance())
