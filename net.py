import networkx as nx


class Network:
    
    def __init__(self):
        ''' Constructs an empty network. '''
        self.Graph = nx.MultiDiGraph()
    
    def add_node(self, n):
        ''' Adds a node with the name n. '''
        self.Graph.add_node(n)
    
    
    def add_road(self, road):
        ''' Adds a road to the network. '''
        road.Graph = self
        self.Graph.add_edge(road.src, road.dest, road=road)

    def add_roads_from(self, roads):
        ''' Adds roads to the network. '''
        edges = len(roads) * [None] 
        for i, road in enumerate(roads):
            edges[i] = (road.src, road.dest, {'road': road, 'free_flow_time': road.free_flow_time})
            road.Graph = self
        self.Graph.add_edges_from(edges)
    
    def remove_road(self, n1, n2):
        ''' Removes road from n1 to n2. '''
        self.Graph.remove_edge(n1, n2)
    
    def remove_roads_from(self, roads):
        ''' Removes roads in list of pairds roads. '''
        self.Graph.remove_edges_from(roads)
    
    def draw(self, save=None):
        ''' Draws/Saves a visual representation of the network. '''
        plt.clf()
        nx.draw(self.Graph, with_labels=True, node_color='lightgrey', font_weight='bold', font_color='black')
        plt.show()
        if save is not None:
            plt.savefig(save)

    def get_roads_from_node(self,node):
        '''Gets a list of roads outwards from any given node'''
        roads = self.Graph.edges(node) 
        return roads