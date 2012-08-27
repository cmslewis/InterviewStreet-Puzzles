
INFINITY = -1

def DijkstraShortestPath(G, start, end):
  

def main():
  numCities, numRoads = [int(n) for n in raw_input().split()]
  
  cityNodes = dict()
  for i in range(numRoads):
    # Read in the next directed edge from standard input.
    city1, city2, distance = [int(n) for n in raw_input().split()]
  
    # Initialize a dictionary for each city ID if we haven't seen it before. 
    if city1 not in cityNodes: cityNodes[city1] = dict()
    if city2 not in cityNodes: cityNodes[city2] = dict()
  
    # Since we're building an undirected (or bidirectional) graph, we need to 
    # insert the current directed edge going in both directions.
    cityNodes[city1][city2] = distance
    cityNodes[city2][city1] = distance
  
  print
  for city in cityNodes:
    print city, ":", cityNodes[city]
  print
  
  # 1. Compute ds and dt using Dijkstra's algorithm.
  # 2. Find the bridges:
  #    a. First find all the optimal edges by iterating over all edges e=(u,v), 
  #       and storing the edges such that ds(u)+length(e)+dt(v)=OPT.
  #    b. Sort all the optimal edges by ds(u) and ds(v). Use the criterion from 
  #       above to find the bridges.
  # 3. Find the islands.
  #    a. One way (the hard way) is to run a modified version of Dijkstra.
  #    b. A smarter and shorter alternative is to just run multiple depth-first 
  #       searches from s and from the far end of each bridge. It's up to the 
  #       reader to figure out how to do so.
  # 4. Find the bypassing paths.
  #    a. Initialise your favourite range-update data structure.
  #    b. Iterate over all the non-bridge edges. If e=(u,v) is an edge crossing 
  #       from island i to island j>i, then range-update 
  #       bypass(i),bypass(i+1),...,bypass(j-1) such that they are no more than 
  #       ds(u)+length(e)+dt(v).
  # 5. Process all the queries. If the edge in question is not a bridge, then we 
  #    simply return the optimal length. Otherwise, we query the range-update 
  #    data structure to find the best bypass length.
  
  
if __name__ == "__main__":
  main()