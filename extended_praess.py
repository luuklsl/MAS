import matplotlib.pyplot as plt
import random as rand

from road import Road
from car import Car
from net import Network

if __name__ == "__main__":

	carList = []
	road_result = [list(),list(),list(),list(),list(),list()]
	roadList = dict()

	nodeList = ["Start","End","A","B"]
	roads = [['Start', 'A', lambda N: 11 + N/20, 'Start-A'], 
			['Start', 'B', lambda N: 22 + N/10, 'Start-B'],
			['A', 'B', lambda N: 9 + N/20, 'A-B'],
			['B', 'A', lambda N: 9 + N/20, 'B-A'],  #we assume bi-directional roads to be independent, but same travel time
			['A', 'End', lambda N: 14 +N/5, 'A-End'],
			['B', 'End', lambda N: 12 + N/10, 'B-End'] ]




	Graph = Network()
	for node in nodeList:
		Graph.add_node(node)

	x = 0
	for road in roads:
		roadList.update({str(road[0]) + str(road[1]): Road(x, road[0],road[1],road[2],road[3])})
		x +=1

	for x in list(roadList):
		Graph.add_road(roadList[x], weight_=roadList[x].get_time())

	avg_travel_time_per_N = []

	# for n in range(1, 2001):
	n = 1000

	searchAlgorithm = "Ego"
	# carList = []
	for i in range(n): 
		carList.append(Car(i, searchAlgo=searchAlgorithm))

	
	
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
					car.time_taken += car.travel_time

				else:
					notAtDest.pop(notAtDest.index(car))


			elif (car.travel_time<=0 and len(car.travel_plan)!=0):
				car.position = car.current_road.dest
				car.current_road.traffic_intensity -= 1
				if not (car.pop()):
					
					car.travel_plan.pop(0) #pop first item in travel plan
					x = car.travel_plan
					car.current_road = roadList[x[0]+x[1]]
					car.current_road.traffic_intensity +=1
					car.travel_time = car.current_road.get_time()
					car.time_taken += car.travel_time


				else:
					notAtDest.pop(notAtDest.index(car))

			for x, road in roadList.items():
				Graph.set_edge_attr((road.src, road.dest), road.get_time())
		
		x = 0
		for road in roadList.keys():
			road_result[x].append(roadList[road].traffic_intensity)
			# print (road_result[x], roadList[roads].get_time(), x)
			x+=1
		max_itter +=1

	# for x in range(len(road_result)):
		# print (len(road_result[x]))
		# print (road_result[x])


	total = 0
	for car in carList:
		total +=  car.time_taken
	total = total/(len(carList))
	avg_travel_time_per_N.append(total)

	# print ("another N done: " + str(n))
 
	print(avg_travel_time_per_N)

	f = open(str(n) + str(searchAlgorithm)+  "traffic_intensity.txt", 'w')
	# for x in range(len(avg_travel_time_per_N)):
		# f.write(str(x+1)+ ", " +str(avg_travel_time_per_N[x]) + "\n")
	for x in range(len(road_result)):
		f.write(str(roads[x][0])+ str(roads[x][1])+", " + str(road_result[x])+ "\n")
	f.close()






	# for car in carList:
	# 	print(car.travel_time, car.current_road, car.identifier, car.time_taken)

	# total = 0
	# for car in carList[:int(n/2)]:
	# 	total +=  car.time_taken
	# total = total/(len(carList)/2)
	# print ("Average Social: "+ str(total))
	# total = 0
	# for car in carList[int(n/2):]:
	# 	total +=  car.time_taken
	# total = total/(len(carList)/2)
	# print ("Average Egoist: " + str(total))

	# for x, road in roadList.items():
		# print (road.traffic_intensity)