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
        for vertex in self.vertices.values():
            vertex.d = float('inf')
            vertex.previous = None
        start.distance = 0
        
        for i in range(len(self.vertices.values())):
            for start in self.adjancencies.keys():
                for end in self.adjancencies[start]:
                    self.relax(self.vertices[start], self.vertices[end[0]], end[1])
        
        for start in self.adjancencies.keys():
            for end in self.adjancencies[start]:
                if self.vertices[end[0]].distance > self.vertices[start].distance + end[1]:
                    return False
        
        return True


    def relax(self, first, second, weight):
        if second.distance > first.distance + weight:
            second.distance = first.distance + weight
            second.previous = first

    def print_path(self, start, vertex):
        if vertex == start:
            print(start, end=" ")
        elif vertex.previous == None:
            print(f"No path from {start} to {vertex} exists.")
        else:
            self.print_path(start,vertex.previous)
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
    my_graph = build_graph_1()
    my_graph.bellman_ford(my_graph.vertices["s"])
    for vertex in my_graph.vertices.values():
        print(f"{vertex.name}: {vertex.distance}", end=" | PATH: ")
        my_graph.print_path(my_graph.vertices["s"], vertex)
        print()
    
main()