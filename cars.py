import logging
ENGINE_TYPE = {
	1: "Gasoline",
	0: "Diesel"
}

class EnvironmentalError(Exception):
	pass 

class Car:
	def __init__(self, brand, tank_capacity, tanked_fuel, engine_type):
		if tank_capacity < tanked_fuel:
			raise ValueError("You cannot create car with fuel amount above its' tank capacity.")
		self.brand = brand
		self.tank_capacity = tank_capacity
		self.tanked_fuel = tanked_fuel
		self.engine_type = ENGINE_TYPE[engine_type]
		logging.basicConfig(level=logging.INFO)
		logging.info(f'New car of brand {self.brand}, with tank full in {round(self.tanked_fuel/self.tank_capacity*100,1)}%.')

	def fill_tank(self, liters = None):
		if self.engine_type == 'Diesel':
			raise EnvironmentalError("ON fuel not available,because of environmental restrictions. Change engine as soon, as possible.")
		if liters:
			if self.tanked_fuel+liters > self.tank_capacity:
				raise ValueError("You cannot fill tank over its capacity!")
			else:
				self.tanked_fuel = self.tanked_fuel + liters 
		else:
			self.tanked_fuel = self.tank_capacity

	def empty_tank(self, limit):
		if limit >= 0 and limit <= 1 and type(limit) == float:
			lost_liters = self.tanked_fuel * (1-limit)
			self.tanked_fuel = self.tanked_fuel * limit
		else:
			logging.error("Limit must be between 1 and 0!")
		return lost_liters 

	def __repr__(self):
		return f'<Car object at {hex(id(self))} registered under the {self.brand} brand, with tank full in {round(self.tanked_fuel/self.tank_capacity*100,1)}%>'
