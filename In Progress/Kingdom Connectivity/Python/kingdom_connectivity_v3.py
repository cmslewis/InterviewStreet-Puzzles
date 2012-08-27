
from collections import Counter

INFINITE_PATHS = -1

class Kingdom:
  
  def __init__(self, numCities):
    self.numCities = numCities
    self.cities    = dict()
    
    # Initialize a city node for each city ID in the range [1, N]. 
    for cityID in range(1, numCities+1):
      self.cities[cityID] = City(cityID)
    
  
  
  def addRoad(self, fromCityID, toCityID):
    # Add the child ID to this city's array of children.
    self.cities[fromCityID].addChildCity(toCityID)
    
    # Add this city's ID to the child's array of parents.
    self.cities[toCityID].addParentCity(fromCityID)
  
  def countPaths(self, fromCityID, toCityID):
    # Using a reverse DFS, label all cities that can reach the destination. 
    self._labelReachableCities(toCityID)
    
    # Topologically sort the cities between the source city and the destination 
    # city, in order of increasing distance from the source city (here, each 
    # road effectively has unit length, so the distance between two cities is 
    # synonymous with the minimum number of hops necessary to traverse from one 
    # to the other).
    sortedCityIDs = self._getSortedDestinations(fromCityID)
    # print sortedCityIDs
    
    # Store the source city for efficiency.
    sourceCity = self.cities[fromCityID]
    
    # Initialize the array for dynamic programming.
    D = dict().fromkeys(sortedCityIDs, 0)
    
    if fromCityID not in D or toCityID not in D:
      return 0
    
    for cityID in sortedCityIDs:
      city = self.cities[cityID]
      #print "\nCity #%d" % cityID
      #print "d_1_k =", sourceCity.children[cityID]
      
      #city = self.cities[cityID]
      
      # If we've already counted this city's paths, then we've found a cycle, 
      # and there are infinitely many paths from the source city to the 
      # destination.
      if city.alreadyCounted == True:
        return INFINITE_PATHS
      
      city.alreadyCounted = True
      
      # Add the number of roads connecting the source city to the current city.
      D[cityID] += sourceCity.children[cityID]
      
      # For each parent of the current city, calculate the number of distinct 
      # paths that the parent city contributes as the number of unique paths 
      # already calculated for that city, times the number of roads connecting 
      # that city with the current city.
      for parentCityID, numRoads in city.parents.items():
        parentCity = self.cities[parentCityID]
        
        parentCity.alreadyCounted = True
        
        if parentCity.status == City.VISITED:
          #print "parentCityID =", parentCityID, ", numRoads =", numRoads
          D[cityID] += numRoads * D[parentCityID]
          
      #print "D[%d] = %d" % (cityID, D[cityID])
    #print D
    
    # Return the number of unique paths from the source city to the destination.
    return D[toCityID]
  
  
  def _labelReachableCities(self, currCityID):
    currCity = self.cities[currCityID]
    
    # Mark the current city as visited for future reference, and add its ID to 
    # the set of source cities that can reach the destination node where we 
    # started this reverse DFS.
    currCity.status = City.CAN_REACH_TARGET
    # sourceCityIDs.add(currCityID)
    
    # Continue the reverse DFS to all unvisited parents of the current city. 
    for parentCityID in currCity.parents.keys():
      if self.cities[parentCityID].status == City.UNVISITED:
        self._labelReachableCities(parentCityID)
    
  
  def _getSortedDestinations(self, sourceCityID):
    sortedCityIDs = []
    self._recGetSortedDestinations(sourceCityID, sortedCityIDs)
    return list(reversed(sortedCityIDs))
  
  def _recGetSortedDestinations(self, currCityID, sortedCityIDs):
    currCity = self.cities[currCityID]
    
    # Mark the current city as visited for future reference
    currCity.status = City.VISITED
    
    # Continue the DFS to all children of the current city.
    for parentCityID in currCity.children.keys():
      if self.cities[parentCityID].status == City.CAN_REACH_TARGET:
        self._recGetSortedDestinations(parentCityID, sortedCityIDs)
    
    # The first city that will reach this line is the one farthest away from the 
    # original source city. Closer cities will be added as the recursion 
    # backtracks. The result will be a list of city IDs sorted in order of 
    # decreasing distance from the original source node.
    sortedCityIDs.append(currCityID)
  

class City:
  
  UNVISITED        = 0
  CAN_REACH_TARGET = 1
  VISITED          = 2
  
  def __init__(self, id):
    self.id       = id
    self.parents  = Counter()
    self.children = Counter()
    self.status   = City.UNVISITED
    self.alreadyCounted = False
  
  def __repr__(self):
    if self.status == City.UNVISITED:
      return "City<id: %d, status: UNVISITED>" % (self.id)
    if self.status == City.VISITED:
      return "City<id: %d, status: VISITED>" % (self.id)
    
    return "City<id: %d, status: CAN_REACH_TARGET>" % (self.id)
  
  def addChildCity(self, childID):
    self.children[childID] += 1
  
  def addParentCity(self, parentID):
    self.parents[parentID] += 1
  


def main():
  # Read in the number of cities and the number of edges.
  numCities, numEdges = [int(token) for token in raw_input().split()]
  
  # Initialize a new kingdom with the specified number of cities.
  kingdom = Kingdom(numCities)
  
  # Read in and create the appropriate edges between cities.
  for i in range(numEdges):
    fromCityID, toCityID = [int(cityID) for cityID in raw_input().split()]
    
    # Add the specified one-way road to the kingdom.
    kingdom.addRoad(fromCityID, toCityID)
  
  # Specify the IDs of the source and destination cities.
  sourceCityID = 1
  destCityID   = numCities
  
  # Report the number of unique paths existing between the specified source and 
  # destination cities, or report "INFINITE PATHS" if a cycle was found.
  numPaths = kingdom.countPaths(sourceCityID, destCityID)
  if numPaths == INFINITE_PATHS:
    print "INFINITE PATHS"
  else:
    print numPaths

if __name__ == "__main__":
  main()
