import matplotlib.pyplot as plt
import random as rand

from road import Road
from car import Car
from net import Network

if __name__ == "__main__":

	carList = []
	nodeList = []
	roadList = dict()

	roads = [['Start', 'A', lambda N: 10 + N/20, 'Start-A'], 
			['Start', 'B', lambda N: 20 + N/10, 'Start-B'],
			['A', 'B', lambda N: 8 + N/20, 'A-B'],
			['B', 'A', lambda N: 20 + N/5, 'B-A'],
			['A', 'End', lambda N: 10 +N/5, 'A-End'],
			['B', 'End', lambda N: 10 + N/10, 'B-End'] ]

	Graph = Network()

	Graph.add_node('Start')
	Graph.add_node('End')
	Graph.add_node('A')
	Graph.add_node('B')

	x = 0
	for road in roads:
		roadList.update({str(road[0]) + str(road[1]): Road(x, road[0],road[1],road[2],road[3])})
		x +=1

	for x in list(roadList):
		Graph.add_road(roadList[x], weight_=roadList[x].get_time())

	for i in range(5000): 
		carList.append(Car(i, searchAlgo="Social"))
	for i in range(5000, 10000):
		carList.append(Car(i, searchAlgo="Ego"))

	pass
		# print(Graph.get_roads_from_node("Start"))
		# x.position = roadList[5]
		# x.travel_time = x.current_road.get_time() #this works because the car(x) position is set on a Road Obj, meaning I can also access that road's public funcs and vars
		# print (x.travel_time)
		# t = roadList[0].get_time()
		# x.travel_time = t
		# print (x.travel_time)
		# x.update_position()
		# print (x.travel_time)
		# print(x.position)
		# A = Graph.get_roads_from_node(None)
		# print(A)

		# Graph.get_edge_attr(("Start","B"))
		# roadList[4].traffic_intensity = 300
		# Graph.set_edge_attr(("A","End"), roadList['AEnd'].get_time())
		# Graph.get_edge_attr(("A","End"))


		# x.travel_time=1
		# print (x.position.dest, x.travel_time)

		#print (Graph.get_roads_from_node("Start"))
		#print (nx.get_edge_attributes(Graph, 'name'))
		#roadList[2].travel_time
		#print(roadList[0].get_time())
		# neighb = list(Graph.neighbours("A"))
		# print (neighb)
	
	notAtDest = list(carList) #this way we don't get any problems with notAtDest being a reference copy instead of a data-copy
	# print(len())
	max_itter=0
	while (len(notAtDest)>0 and max_itter<=10000000):
		"""As long as not all cars have arrived at their destination we keep on itterating"""

		for car in notAtDest:
			car.update()

			if (car.travel_time <= 0 and car.travel_plan == []): #do we have an empty list of following nodes?

				if car.current_road != None: #if we previously were on a road, get the roads destination
					node = car.current_road.dest
					car.current_road.traffic_intensity -= 1
					car.position = node
					#if current rode == None, node = car.position (we haven't done anything yet)
				else:
					node = car.position


				if not (car.pop()):
					x = Graph.dijkstra_path(node, car.destination) #does not waste recources on useless calls!

					if (car.search == "Ego"):
						car.travel_plan = x
						car.current_road= roadList[x[0]+x[1]]

					elif (car.search == "Social"):
						car.current_road = roadList[x[0]+x[1]]

					car.travel_time = car.current_road.get_time()	
					car.current_road.traffic_intensity += 1
					# if (max_itter%10==0):
						# print (car.travel_time)
					car.time_taken += car.travel_time

				else:
					notAtDest.pop(notAtDest.index(car))


			elif (car.travel_time<=0 and len(car.travel_plan)!=0):
				car.position = car.current_road.dest

				if not (car.pop()):
					car.current_road.traffic_intensity -=1
					car.travel_plan.pop(0) #pop first item in travel plan
					x = car.travel_plan
					# print (x)
					car.current_road = roadList[x[0]+x[1]]
					car.current_road.traffic_intensity +=1
					car.travel_time = car.current_road.get_time()
					car.time_taken += car.travel_time


				else:
					notAtDest.pop(notAtDest.index(car))
			for x, road in roadList.items():
				Graph.set_edge_attr((road.src, road.dest), road.get_time())
		
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



		# print (len(notAtDest))
		max_itter +=1

		# break  #only remove this after you are SURE that you won't get hanging on the while loop! (eg, add a max_itter counter in the while)
	total = 0
	for car in carList[:5000]:
		print(car.travel_time, car.current_road, car.identifier, car.time_taken)
		total +=  car.time_taken
	total = total/(len(carList)/2)
	print ("Average Social: "+ str(total))
	total = 0
	for car in carList[5000:]:
		total +=  car.time_taken
	total = total/(len(carList)/2)
	print ("Average Egoist: " + str(total))

	# for x, road in roadList.items():
		# print (road.traffic_intensity)