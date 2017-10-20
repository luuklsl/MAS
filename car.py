class Car:

	def __init__(self, identifier, dest="End", start="Start", searchAlgo="AStar"):
		self.destination = dest
		self.identifier = identifier
		self.position = start
		self._searchAlgo = searchAlgo
		self.travel_time = int
		self.current_road = ""
		#self.prev_node/road?
	


	def update(self):
		"""Update self, check for road_switch_cases"""
		self._update_position()

		# if self.travel_time <= 0:   #if we done with current_road
		# 	route = self._Astar_search()
			

	def _update_position(self):   #please use only within car_object
		self.travel_time = self.travel_time-1

	@property
	def search(self):
		return (self._searchAlgo)
	
	@search.setter
	def search(self, value):
		if (value == "Social" or value == "AStar"):
			self._searchAlgo = value
		else:
			raise ValueError ("Value was not AStar or Social")



	def Astar_search(self):
		"""A* search for our network."""
		pass

	
	def __repr__(self):				#this basically defines what is printed if you call "print(Obj)"
		return 'Car(destination:\'{}\', identifier:\'{}\', )'.format(self.destination, self.identifier)
