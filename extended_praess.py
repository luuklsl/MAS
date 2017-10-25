import matplotlib.pyplot as plt
import random as rand

from road import Road
from car import Car
from net import Network

if __name__ == "__main__":

	carList = []

	road_result = [list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list(),list()]
	nodeList = ['Start', 'A', 'B', 'C', 'D', 'E', 'End']

	roadList = dict()
	roads = [['Start', 'A', lambda N: 10 + N/20, 'Start-A'], 
	 		['Start', 'D', lambda N: 10 + N/20, 'Start-D'],

	 		['A', 'D', lambda N: 9 + N/10, 'A-D'],
	 		['D', 'A', lambda N: 9 + N/10, 'D-A'],  

	 		['D', 'C', lambda N: 8 + N/5, 'D-C'],
	 		['C', 'D', lambda N: 8 + N/5, 'C-D'],

	 		['A', 'C', lambda N: 10 + N/5, 'A-C'],
	 		['C', 'A', lambda N: 10 + N/5, 'C-A'], 

	 		['A', 'B', lambda N: 9 + N/20, 'A-B'],
	 		['B', 'A', lambda N: 9 + N/20, 'B-A'], 

	 		['B', 'C', lambda N: 9 + N/5, 'B-C'],
	 		['C', 'B', lambda N: 9 + N/5, 'C-B'], 

	 		['C', 'E', lambda N: 7 + N/5, 'C-E'],
	 		['E', 'C', lambda N: 7 + N/5, 'E-C'], 

	 		['D', 'E', lambda N: 10 + N/20, 'B-C'],
	 		['E', 'D', lambda N: 10 + N/20, 'C-B'],

	 		['B', 'E', lambda N: 10 + N/10, 'B-E'],
	 		['E', 'B', lambda N: 10 + N/10, 'E-B'], 

	 		['E', 'End', lambda N: 12 + N/20, 'A-End'],
	 		['B', 'End', lambda N: 12 + N/20, 'B-End'] ]


	Graph = Network()

	for x in nodeList:
		Graph.add_node(x)

	x = 0
	for road in roads:
		roadList.update({str(road[0]) + str(road[1]): Road(x, road[0],road[1],road[2],road[3])})
		x +=1
	

	for x in list(roadList):
		Graph.add_road(roadList[x], weight_=roadList[x].get_time())


	# Graph.draw()

	avg_travel_time_per_N = []

	for n in range(1, 2001):
		if n%20==0:# n = 100000

			searchAlgorithm = "Ego"
			carList = []
			for i in range(n): 
				carList.append(Car(i, searchAlgo=searchAlgorithm))
			#if running the code for a certain range of N: don't forget to reset carlist every loop
			
			
			notAtDest = list(carList) #this way we don't get any problems with notAtDest being a reference copy instead of a data-copy
			# print(len())
			max_itter=0
			while (len(notAtDest)>0 and max_itter<=10000000):
				"""As long as not all cars have arrived at their destination we keep on itterating"""

				for car in notAtDest:
					car.update()

					if (car.travel_time <= 0 and car.travel_plan == []): #do we have an empty list of following nodes?

						if car.current_road is not None: #if we previously were on a road, get the roads destination
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
				
				# for x in roadList:
					# print (roadList[x].traffic_intensity)
				x = 0
				for road in roadList.keys():
					road_result[x].append(roadList[road].traffic_intensity)
					x+=1
				max_itter +=1


			# for x in range(len(road_result)):
				# print (len(road_result[x]))
				# print (road_result[x])


			total = 0
			for car in carList:
				total +=  car.time_taken
			print (len(carList))
			total = total/(len(carList))
			avg_travel_time_per_N.append(total)

			print ("another N done: " + str(n))
 
	print(avg_travel_time_per_N)

	f = open(str(n) + str(searchAlgorithm)+  "_AVG_Time_complicated.txt", 'w')
	for x in range(len(avg_travel_time_per_N)):
		f.write(str((x+1)*20)+ ", " +str(avg_travel_time_per_N[x]) + "\n")
	# for x in range(len(road_result)):
		# f.write(str(roads[x][0])+ str(roads[x][1])+", " + str(road_result[x])+ "\n")
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