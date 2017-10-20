import networkx as nx
import matplotlib.pyplot as plt

class Main:
    
    def __init__(self, ):
        N_cars: 200
        for x in range(N_cars):
            Car(x)


    def function():
        pass

    def function():
        pass

    def function():
        pass


class Road: #shouldn't road be a subclass of Network, as it is part of that?
    
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


    
class Car:

    def __init__(self, identifier, dest="End", start="Start", searchAlgo="AStar"):
        self.destination = dest
        self.identifier = identifier
        self.position = start
        self._searchAlgo = searchAlgo
        #self.start_time
    
    def update_position(self):
    	self.ticks = self.ticks-1

    @property
    def search(self):
    	return (self._searchAlgo)
    
    @search.setter
    def search(self, value):
    	if (value == "Social" or value == "AStar"):
    		self._searchAlgo = value
    	else:
    		raise ValueError ("Value was not AStar or Social")



    def _Astar_search(self):
        pass
    #Need to rewrite below one to remove car from carList when car has reached their dest 

    
    def __repr__(self):				#this basically defines what is printed if you call "print(Obj)"
        return 'Car(destination:\'{}\', identifier:\'{}\', )'.format(self.destination, self.identifier)


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


carList = []
nodeList = []
roadList = []
roads = [['Start', 'A', lambda N: 10 + N/10, 't=N/10'], ['Start', 'B', lambda N: 45, 't=45'],['A', 'B', lambda N: 0, 't=0'],
    ['B', 'A', lambda N: 10, 't=10'],['A', 'End', lambda N: 45, 't=45'],['B', 'End', lambda N: N/100, 't=N/100'] ]
Graph = Network()

Graph.add_node('Start')
Graph.add_node('End')
Graph.add_node('A')
Graph.add_node('B')

for road in roads:

    roadList.append(Road(road[0],road[1],road[2],road[3]))
print (roadList)
for x in range(len(roadList)):
    Graph.add_road(roadList[x])


# Graph.draw()





for i in range(10): #above 10e4 you can expect this to get waaay slower
	carList.append(Car(i))

x = carList[5]
print (x.search)
x.search = "Social"
print(x.search)
print (Graph.get_roads_from_node("Start"))
#print (nx.get_edge_attributes(Graph, 'name'))


roadList[2].travel_time
print(roadList[0].get_time())


while (len(carList)>0):
    break

print (carList[200])
#time = get_edge_attributes(G,N)
#print (time)

#print("social:", list(Graph.social_path('Start')))
# print("egoist:", list(Graph.egoist_path('Start')))