class Car:

	def __init__(self, identifier, dest="End", start="Start", searchAlgo="Ego"):
		self.destination = dest
		self.src = start
		self.identifier = identifier
		self.position = start
		self._searchAlgo = searchAlgo
		self.travel_time = 0
		self.current_road = None
		self.travel_plan = []
		self.time_taken = 0
		#self.prev_node/road?
	


	def update(self):
		"""Update self, check for road_switch_cases"""
		self._update_position()

		# if self.travel_time <= 0:   #if we done with current_road
		# 	route = self._Ego_search()
			
	def pop(self):
		return self.destination == self.position

	def _update_position(self):   #please use only within car_object
		self.travel_time = self.travel_time-1

	@property
	def search(self):
		return (self._searchAlgo)
	
	@search.setter
	def search(self, value):
		if (value == "Social" or value == "Ego"):
			self._searchAlgo = value
		else:
			raise ValueError ("Value was not Ego or Social")



	def set_road(self,road):
		self.current_road = road

	
	def __repr__(self):				#this basically defines what is printed if you call "print(Obj)"
		return 'Car(destination:\'{}\', identifier:\'{}\', )'.format(self.destination, self.identifier)
