class Vehicle:
	def accelerate(self):
	def steer(self):
	def brake(self):

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

class Bike(Vehicle):
  pass


bike = Bike()
bike.accelerate() # error
