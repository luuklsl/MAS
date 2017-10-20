class Car:

    def __init__(self, identifier, dest="End", start="Start", searchAlgo="AStar"):
        self.destination = dest
        self.identifier = identifier
        self.position = start
        self._searchAlgo = searchAlgo
        self.travel_time = 0
        #self.start_time
    
    def update_position(self):
    	self.travel_time = self.travel_time-1

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
