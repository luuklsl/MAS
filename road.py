from net import Network

class Road(Network):
	
	def __init__(self, ident, src, dest, time_func, name=None):
		''' Constructs a Road from src to dest, using the flow function time_func, with a label. '''
		# self.Graph = None
		self.id = ident
		self.name = name
		self.src = src
		self.dest = dest
		self.travel_time = time_func
		self.traffic_intensity = 0

	# def get_time(self):
		# return super().get_edge_attr((self.src, self.dest))

	# def update_trafic_intensity(self, integer):
	# 	self.trafic_intesity += integer
	# 	super().set_edge_attr((self.src, self.dest), self.calc_time())


	def get_time(self):
		return (self.travel_time(self.traffic_intensity))

	def __repr__(self):
		return 'Road: Name \'{}\', time_func:\'{}\'' .format(self.name, self.travel_time)