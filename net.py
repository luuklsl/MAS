import networkx as nx
import matplotlib.pyplot as plt


class Network:
	
	def __init__(self):
		''' Constructs an empty network. '''
		self.Graph = nx.DiGraph()



	def neighbours(self, node):
		"""Queries the graph on it's neighbours, returns dict of dict"""
		return self.Graph[node].keys()

	def add_node(self, n):
		''' Adds a node with the name n. '''
		self.Graph.add_node(n)
	
	def add_road(self, road, weight_):
		''' Adds a road to the network. '''
		road.Graph = self
		# print(weight_)
		self.Graph.add_edge(road.src, road.dest,
				 key=str(road.src) + str(road.dest), weight=weight_)

	

	def draw(self, save=None):
		''' Draws/Saves a visual representation of the network. '''
		plt.clf()
		nx.draw(self.Graph, with_labels=True, node_color='orange', font_weight='bold', font_color='black')
		plt.show()
		if save is not None:
			plt.savefig(save)

	# def get_node_attr(self, node_c):
	# 	return self.Graph.nodes(node_c)	

	# def set_node_attr(self, node_n):
	# 	self.Graph.set_node_attributes(node_n)


	def get_edge_attr(self, nodes):
		"""get edge attribute from nodes, only weight as this is important for our case"""
		ret = nx.get_edge_attributes(self.Graph, "weight")
		print ("Getting attribute from edge from {}: {}".format(nodes,ret[nodes]))
		return (ret[nodes])

	def set_edge_attr(self, nodes, weight_):
		"""Set the edge attribute between two nodes (u, v) with a given weight"""
		self.Graph.edge[nodes[0]][nodes[1]]['weight'] = weight_
		# print("this")



	def get_roads_from_node(self,node):
		'''Gets a list of roads outwards from any given node'''
		roads = self.Graph.edges(node) 
		return roads



	def dijkstra_path(self, src, dest):
		# print (self.Graph[src])
		x = nx.dijkstra_path(self.Graph, src, dest)
		return x