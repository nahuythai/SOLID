class Call:
	@abstract
	def call():

class Wifi:
	@abstract
	def wifi():

class 3G:
	@abstract
	def use3g()

class ModernPhone(Call, 3G, Wifi):
  pass

class Telephone(Call)
  pass

class S40Phone(Call, 3G)
  pass
