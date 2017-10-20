import matplotlib.pyplot as plt

from road import Road
from car import Car
from net import Network

if __name__ == "__main__":

	carList = []
	nodeList = []
	roadList = []

	roads = [['Start', 'A', lambda N: 10 + N/10, 'Start-A'], 
			['Start', 'B', lambda N: 45, 'Start-B'],
			['A', 'B', lambda N: 0, 'A-B'],
	    	['B', 'A', lambda N: 10, 'B-A'],
	    	['A', 'End', lambda N: 45, 'A-End'],
	    	['B', 'End', lambda N: N/100, 'B-End'] ]

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

	for i in range(1): 
		carList.append(Car(i))

	for x in carList: 
		print(Graph.get_roads_from_node("Start"))
		x.position = roadList[0]
		t = roadList[0].get_time()
		x.travel_time = t
		print (x.travel_time)
		x.update_position()
		print (x.travel_time)
		print(x.position)

	print (roadList[1].dest)


	#print (carList[0])
	##print (x.search)
	#x.search = "Social"
	#print(x.search)
	#print (Graph.get_roads_from_node("Start"))
	#print (nx.get_edge_attributes(Graph, 'name'))
	#roadList[2].travel_time
	#print(roadList[0].get_time())
	notAtDest = carList
	while (len(notAtDest)>0):
	    """As long as not all cars have arrived at their destination we keep on itterating"""
	    break

