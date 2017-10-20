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
		x.travel_time = x.position.get_time() #this works because the car(x) position is set on a Road Obj, meaning I can also access that road's public funcs and vars
		# print (x.travel_time)
		# t = roadList[0].get_time()
		# x.travel_time = t
		# print (x.travel_time)
		# x.update_position()
		# print (x.travel_time)
		# print(x.position)
 
	print (roadList[1].dest)


	#print (carList[0])
	##print (x.search)
	#x.search = "Social"
	#print(x.search)
	#print (Graph.get_roads_from_node("Start"))
	#print (nx.get_edge_attributes(Graph, 'name'))
	#roadList[2].travel_time
	#print(roadList[0].get_time())

	
	notAtDest = list(carList) #this way we don't get any problems with notAtDest being a reference copy instead of a data-copy


	while (len(notAtDest)>0):
		"""As long as not all cars have arrived at their destination we keep on itterating"""

		for car in carList:
			car.update()

			if car.travel_time == 0:
				car.Astar_search()




		#first we want to itterate through our carList
			#update them cars!
			#now check if car.travel_time == 0 if so
				#we kinda wanna know what the next best option is (if social)
				#or just get what we already decided (both options obvs based on our search strat)
				#if we are making any new choice, be sure to update both the old road and the new road so we are keeping track!
				# also, set new timer based on road.get_time() for the car
		# we can now check anything on for roads as well, if we want (like if we are busy?)
		#now is also the best time to get most of the stats that we need for graphs later on
		

		#start a new round of iterations, aka t+=1 (this is mainly for timekeeping for cars that start later on (which itself can be modeled after a p.d.f.))	






		break  #only remove this after you are SURE that you won't get hanging on the while loop! (eg, add a max_itter counter in the while)
