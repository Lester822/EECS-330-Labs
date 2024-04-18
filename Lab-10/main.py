'''
Author: Michael Stang
Date: 04-18-24
Lab: lab 10
Last modified: 04-18-24
Purpose: Implementation of search for shortest path of graphs
'''

import heapq

class Vertex:
    """A class to represent our basic vertices of the graphs"""
    def __init__(self, name):
        # This is just a container to hold data
        self.name = name  # Holds a name
        self.color = "white"  # the color
        self.distance = float('inf')  # the distance for search
        self.previous = None  # The previous element

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __repr__(self):
        return self.name

class AdjacencyList:
    """A class to represent our graphs with built in methods for searching"""
    def __init__(self):
        self.vertices = {}  # Holds all the verticies as a dictonary based on string
        self.adjancencies = {}  # Holds all of the adjacencies
        self.time = 0  # The current time (used for dfs)

    def add_vertex(self, name):
        self.vertices[name] = Vertex(name)  # Adds a vertex with the passed in name to our list of vertices
        self.adjancencies[name] = []  # Adds the same vertex to our adjacencies dictonary but with no connections yet
    
    def add_adjacency(self, vertex_1, vertex_2, weight):  # takes in names of two vertices and forms a unidirectional edge
        self.adjancencies[vertex_1].append([vertex_2, weight])  # Adds vertex 2's name to the list of adjacencies for vertex 1
        #self.adjancencies[vertex_2].append([vertex_1, weight])  # The same but the other way around
        # adjancencies are accessed as self.adjancencies["string name of vertex"][#] where # = 0 for the vertex, and # = 1 for the weight
    
    def bellman_ford(self, start):
        """Method for finding the shortest path for all verticies from the given start vertex"""

        # Start by resting the vertices
        for vertex in self.vertices.values():
            vertex.d = float('inf')
            vertex.previous = None
        start.distance = 0  # Sets the distance of our start vertex to 0
        
        for i in range(len(self.vertices.values())):  # For each vertex in the graph
            for start in self.adjancencies.keys():
                for end in self.adjancencies[start]:  # And for every edge (which is a double for loop since they are a dictonary)
                    relax(self.vertices[start], self.vertices[end[0]], end[1]) # Edges are represented as {"start vertex name": ["end vertex name", weight]}.
                                                                                    # This means end[0] is the end vertex and end[1] is the weight
        
        for start in self.adjancencies.keys():
            for end in self.adjancencies[start]: # Loops through each edge again
                if self.vertices[end[0]].distance > self.vertices[start].distance + end[1]: # Detection for negative weight cycles
                    return False
        
        return True  # Returns true if there is a meaningingful solution


    def dijkstra(self, start):
        for vertex in self.vertices.values(): # Resets each vertex
            vertex.distance = float('inf')
            vertex.previous = None
        start.distance = 0  # Sets the distance of our start vertex to 0
        
        completed = []  # used to track completed vertices
        queue = []  # list that will hold our priority queue

        # Adds each vertex to the queue
        for vertex in self.vertices.values():
            heapq.heappush(queue, vertex)

        # print(queue) # Debug
        
        # While we still have vertices in the queue
        while len(queue) > 0:
            
            u = heapq.heappop(queue)  # Remove the top

            # print(u) # Debug

            completed.append(u)  # Mark it as complete

            for vertex_name in self.adjancencies[u.name]: # Goes through each edge
                vertex = self.vertices[vertex_name[0]] 
                
                if relax(u, vertex, vertex_name[1]):  # Relaxes it, and if it does something...
                    heapq.heapify(queue) # Update the heap
            
        



def relax(first, second, weight):
    """Helper function for both approaches"""
    if second.distance > first.distance + weight: # If the second's distance is more than the current vertex's plus the distance between the two, it's shorter to go that way
        second.distance = first.distance + weight  # So update the distance
        second.previous = first  # And the previous
        return True # Return if it updated anything
    else:
        return False

def print_path(start, vertex):
    """Print the minimum path after its been calculated"""
    if vertex == start: # Base case: We're at the start
        print(start, end=" ")
    elif vertex.previous == None:  # Base Case: The two don't connect
        print(f"No path from {start} to {vertex} exists.")
    else:  # Otherwise, just print the vertex and then recursively call it
        print_path(start,vertex.previous)
        print(vertex, end=" ")
            
        
        


def build_graph_1():
    """Builds the first graph"""
    my_list = AdjacencyList()
    [my_list.add_vertex(n) for n in ["s", "t", "x", "y", "z"]]  # List agancency to add all verticies :)
    
    my_list.add_adjacency("s", "t", 6)
    my_list.add_adjacency("s", "y", 7)
    my_list.add_adjacency("t", "x", 5)
    my_list.add_adjacency("t", "y", 8)
    my_list.add_adjacency("t", "z", -4)
    my_list.add_adjacency("x", "t", -2)
    my_list.add_adjacency("y", "x", -3)
    my_list.add_adjacency("y", "z", 6)
    my_list.add_adjacency("z", "x", 7)
    my_list.add_adjacency("z", "s", 2)

    return my_list

def build_graph_2():
    """Builds the second graph"""
    my_list = AdjacencyList()
    [my_list.add_vertex(n) for n in ["s", "t", "x", "y", "z"]]  # List agancency to add all verticies :)
    
    my_list.add_adjacency("s", "t", 10)
    my_list.add_adjacency("s", "y", 5)
    my_list.add_adjacency("t", "y", 2)
    my_list.add_adjacency("t", "x", 1)
    my_list.add_adjacency("x", "z", 4)
    my_list.add_adjacency("y", "t", 3)
    my_list.add_adjacency("y", "x", 9)
    my_list.add_adjacency("y", "z", 2)
    my_list.add_adjacency("z", "x", 6)
    my_list.add_adjacency("z", "s", 7)

    return my_list

def main():

    # GRAPH 1 (BELLMAN FORD)
    print("GRAPH 1: BELLMAN FORD\n") # Header
    my_graph = build_graph_1()  # Makes graph
    my_graph.bellman_ford(my_graph.vertices["s"]) # Calcluates the shortest path for each using bellman ford
    for vertex in my_graph.vertices.values():  # Loops to print details for each vertex
        print(f"{vertex.name}: {vertex.distance}", end=" | PATH: ")
        print_path(my_graph.vertices["s"], vertex)
        print()


    # GRAPH 2 (DIJKSTRA'S) [same as above, but with different graph and Dikstra's alg.]
    print("\n\nGRAPH 2: DIJKSTRA\n")
    my_second_graph = build_graph_1()
    my_second_graph.dijkstra(my_second_graph.vertices["s"])
    for vertex in my_second_graph.vertices.values():
        print(f"{vertex.name}: {vertex.distance}", end=" | PATH: ")
        print_path(my_second_graph.vertices["s"], vertex)
        print()


    
main()