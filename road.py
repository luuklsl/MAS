class Road:
	
	def __init__(self, src, dest, time_func, name=None):
		''' Constructs a Road from src to dest, using the flow function time_func, with a label. '''
		# self.Graph = None
		self.name = name
		self.src = src
		self.dest = dest
		self.travel_time = time_func
		self.traffic_intensity = 20

	def get_time(self):
		return (self.travel_time(self.traffic_intensity))

	def __repr__(self):
		return 'Road: Name \'{}\'' .format(self.name)