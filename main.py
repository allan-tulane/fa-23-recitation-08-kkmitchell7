from collections import deque
from heapq import heappush, heappop, heapify

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    distance = {}
    smallestsol = {}
    for vertex in graph:
        distance[vertex] = (float('inf'), 0)
    
    distance[source] = (0, 0)

    
    #need to iterate through all the connections
    for node in graph:
        connections = graph[node]
        for connection in connections:
            if distance[node][0] + connection[1] < distance[connection[0]][0]:
                distance[connection[0]] = (distance[node][0] + connection[1], distance[node][1] + 1)
            if distance[node][0] + connection[1] == distance[connection[0]][0]:
                if distance[node][1] + 1 < distance[connection[0]][1]:
                    distance[connection[0]] = (distance[node][0] + connection[1], distance[node][1] + 1)
    

    return distance

               
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    pathtree = {}
    distance = {}
    for vertex in graph:
        distance[vertex] = float('inf')
    
    distance[source] = 0

    #need to assign weight 1 to each vertex
    
    #need to iterate through all the connections
    for node in graph:
        connections = graph[node]
        for connection in connections:
            if distance[node] < distance[connection]:
                distance[connection] = distance[node] + 1
                pathtree[connection] = node
    return pathtree

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    shortestpath = ''
    currdest = destination
    contloop = True
    
    #need to iterate through until we reach the source node
    while contloop == True:
      contloop = False
      for key in parents:
          if key == currdest:
              shortestpath += parents[key]
              currdest = parents[key]
              contloop = True
    
    return shortestpath[::-1]

