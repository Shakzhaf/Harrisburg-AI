from Vehicle import Vehicle
class Bicycle(Vehicle):
	def __init__(self, top_speed, location, direction):
		super().__init__(5.0 ,top_speed, location, direction)


	def accelerate(self):
		self._current_speed=self._top_speed


	def decelerate(self):
		self._current_speed=0.0
