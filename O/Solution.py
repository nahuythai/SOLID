
class Payment:
	@abstractmethod
	def pay(self)


class DebitPayment(Payment):
	def pay(self):
    # do something
    pass

class CreditPayment(Payment):
	def pay(self):
    #do something
    pass
  
class CashPayment(Payment):
  	def pay(self):
    #do something
    pass
