'''
Author: Michael Stang
Date: 04-11-24
Lab: lab 9
Last modified: 04-11-24
Purpose: Two implementations of MST
'''

import heapq

class Node:
    # Node class to hold values and from trees
    def __init__(self, value):
        self.value = value  # Var to hold the value
        self.parent = None  # Var to hold this node's parent
        self.rank = 0  # Var to hold to rank
    def __repr__(self):
        #return f"[NODE: (Value = {self.value}), Parent = {self.parent if self.parent != self else None}, Rank = {self.rank})]\n"  # A part for nice output
        return self.value
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value

class DistjointSet:
    # Class for the Disjoint Set
    def __init__(self):
        self.sets = set()  # Var to hold the various sets

    def make_set(self, in_node):
        # Makes a new set within the disjoint set
        in_node.rank = 0
        in_node.parent = in_node
        self.sets.add(in_node)

    def union(self, x, y):
        # Combines sets with given nodes
        self.link_set(self.find_set(x), self.find_set(y))

    def link_set(self,x,y):
        # Connects two sets together for the union
        if x.rank > y.rank:  # Checks which has the higher rank
            y.parent = x
        else:
            x.parent = y 
            if x.rank == y.rank:
                y.rank = y.rank + 1

    def find_set(self, x):
        # Finds the node that is the representative of a set with the given node
        if x != x.parent:
            x.parent = self.find_set(x.parent)  # Recursively find it
        return x.parent

class Vertex:
    """A class to represent our basic vertices of the graphs"""
    def __init__(self, name):
        # This is just a container to hold data
        self.name = name  # Holds a name
        self.color = "white"  # the color
        self.key = float('inf')  # the distance for search
        self.previous = None  # The previous element

    def __lt__(self, other):
        return self.key < other.key
    def __gt__(self, other):
        return self.key > other.key
    
    def __repr__(self):
        return self.name

class AdjacencyList:
    """A class to represent our graphs with built in methods for searching"""
    def __init__(self):
        self.vertices = {}  # Holds all the verticies as a dictonary based on string
        self.adjancencies = {}  # Holds all of the adjacencies
        self.time = 0  # The current time (used for dfs)
        self.weight = 0
        self.edges = []
        self.connections = []

    def add_vertex(self, name):
        self.vertices[name] = Vertex(name)  # Adds a vertex with the passed in name to our list of vertices
        self.adjancencies[name] = []  # Adds the same vertex to our adjacencies dictonary but with no connections yet
    
    def add_adjacency(self, vertex_1, vertex_2, weight):  # takes in names of two vertices and forms a unidirectional edge
        self.adjancencies[vertex_1].append([vertex_2, weight])  # Adds vertex 2's name to the list of adjacencies for vertex 1
        self.adjancencies[vertex_2].append([vertex_1, weight])  # The same but the other way around
        # adjancencies are accessed as self.adjancencies["string name of vertex"][#] where # = 0 for the vertex, and # = 1 for the weight

    def mst_kruskal(self):
        """Function to find the MST using kruskal's algorithm"""
        A = DistjointSet()  # Disjoint set to hold our edges
        self.weight = 0  # Resets weight from previous runs
        self.edges = []  # Resets edges from previous runs
        
        nodes = {}  # Makes a set to hold each node
        for vertex in self.vertices:  # Goes through each vertex
            nodes[vertex] = (Node(vertex))  # Makes a node for each vertex
            A.make_set(nodes[vertex])  # Makes a set within the disjoint set for each vertex/node
            for adjacency in self.adjancencies[vertex]:  # Goes through each edge
                if (adjacency[1], adjacency[0], vertex) not in self.edges:  # And if the inverse is not already in the list of edges
                    self.edges.append((adjacency[1], vertex, adjacency[0]))  # Add the edge (with its weight)
        self.edges.sort()  # Sorts the list by weight
        for edge in self.edges:  
            if A.find_set(nodes[edge[1]]) != A.find_set(nodes[edge[2]]):  # If the edges aren't already in the same set in the disjoint set...
                A.union(nodes[edge[1]], nodes[edge[2]])  # Union them together
                self.weight += edge[0]  # Adds the weight of the thing we just added to the weight
                self.connections.append((nodes[edge[1]], nodes[edge[2]]))  # Adds to the list of connections 
        return A

    def mst_prim(self, r):
        self.weight = 0  # Resets weight from previous runs
        self.edges = []  # Resets edges from previous runs
        for v in self.vertices:  # Goes through each vertex
            vertex = self.vertices[v]  # Goes from string of verticies to vertex objects
            vertex.key = float('inf')  # Reset all keys and previous values
            vertex.previous = None  # 
            for adjacency in self.adjancencies[vertex.name]:  # Goes through each adjacency (edge)
                if (adjacency[1], adjacency[0], vertex.name) not in self.edges:  # Assembles a list of edges (just for demo purposes)
                    self.edges.append((adjacency[1], vertex.name, adjacency[0]))
        self.vertices[r].key = 0  # Start vertex has key 0 to ensure it is first
        minheap = [(0, r, self.vertices[r])]  # Initialize priority queue with start vertex
        
        mst = []  # List to store edges
        added = set()  # Track added vertices to avoid duplicates (I may want to change the above to work like this, now that I think of it)

        while minheap:
            key, name, u = heapq.heappop(minheap)
            if name in added:
                continue  # Skip if its there already
            added.add(name)  # Add to our tracking list for what's been added
            if u.previous is not None:  
                mst.append((u.previous, u))
                self.weight += key  # Add up the weight as we go
            
            for v, weight in self.adjancencies[name]:  # Goes through each adjacency
                vertex = self.vertices[v]  # Gets the actual vertex object
                if v not in added and weight < vertex.key:
                    vertex.key = weight
                    vertex.previous = u
                    heapq.heappush(minheap, (vertex.key, v, vertex))  # Adds to the minheap

        return mst




def make_graph():
    """Aseembles the given graph"""
    my_adj = AdjacencyList()
    verticies = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  # Adds vertices
    for vertex in verticies:
        my_adj.add_vertex(vertex)
    
    # Adds edges
    my_adj.add_adjacency("a", "b", 4)
    my_adj.add_adjacency("a", "h", 8)
    my_adj.add_adjacency("b", "h", 12)
    my_adj.add_adjacency("b", "c", 8)
    my_adj.add_adjacency("h", "i", 7)
    my_adj.add_adjacency("i", "c", 2)
    my_adj.add_adjacency("h", "g", 1)
    my_adj.add_adjacency("g", "f", 2)
    my_adj.add_adjacency("g", "i", 6)
    my_adj.add_adjacency("c", "f", 4)
    my_adj.add_adjacency("c", "d", 7)
    my_adj.add_adjacency("d", "e", 9)
    my_adj.add_adjacency("d", "f", 14)
    my_adj.add_adjacency("e", "f", 10)

    return my_adj

def main():
    print("(1) Kruskal's Algorithm Demo")
    graph = make_graph()  # Makes the graph given
    graph.mst_kruskal()  # Calculates the MST
    print(f"Edges: {graph.edges}\nTotal Weight: {graph.weight}\nA =" + "{" + str(graph.connections) + "}")

    graph = make_graph()
    print("\n(2) Prim's Algorithm Demo")
    mst_prim = graph.mst_prim('a')  # Starts prims on vertex 'a'
    print(f"Edges: {graph.edges}\nTotal Weight: {graph.weight}\nA =" + "{" + str(mst_prim) + "}") # Same print as above

main()

    