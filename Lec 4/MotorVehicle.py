from Vehicle import Vehicle
class MotorVehicle(Vehicle):
	def __init__(self, length ,top_speed, location, direction, license_plate, acceleration_factor):
		super().__init__(length, top_speed, location, direction)
		self._license_plate=license_plate
		self._acceleration_factor=acceleration_factor

	def get_acceleration(self):
		return self._acceleration_factor

	def get_license_plate(self):
		return self._license_plate

	def set_license_plate(self,str):
		self._license_plate=str

	def accelerate(self):
		if(self._current_speed<self._top_speed):
			self._current_speed+=self._acceleration_factor * self._top_speed


	def decelerate(self):
		if(self._current_speed>0):
			self._current_speed-=self._acceleration_factor * self._top_speed

	def turn_right(self):
		super().turn_right()
		self.decelerate()

	def turn_left(self):
		super().turn_left()
		self.decelerate()