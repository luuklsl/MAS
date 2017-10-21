import networkx as nx


class Network:
	
	def __init__(self):
		''' Constructs an empty network. '''
		self.Graph = nx.MultiDiGraph()


	def neighbours(self, node):
		"""Queries the graph on it's neighbours, returns dict of dict"""
		return self.Graph[node].keys()

	def add_node(self, n, visited=False):
		''' Adds a node with the name n. '''
		self.Graph.add_node(n, vis_attr = visited)
	
	
	def add_road(self, road):
		''' Adds a road to the network. '''
		road.Graph = self
		self.Graph.add_edge(road.src, road.dest, road=road)

	
	def draw(self, save=None):
		''' Draws/Saves a visual representation of the network. '''
		plt.clf()
		nx.draw(self.Graph, with_labels=True, node_color='lightgrey', font_weight='bold', font_color='black')
		plt.show()
		if save is not None:
			plt.savefig(save)

	def get_node_attr(self, node_c):
		return self.Graph.nodes(node_c)



	def get_roads_from_node(self,node):
		'''Gets a list of roads outwards from any given node'''
		roads = self.Graph.edges(node) 
		return roads