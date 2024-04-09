'''
Author: Michael Stang
Date: 04-05-24
Lab: lab 8
Last modified: 04-05-24
Purpose: Basic implementation of a BFS and DFS
'''

class Queue:
    """A list based implementation of basic queue"""
    def __init__(self):
        self.queue = []  # Var to hold queue
    
    def enqueue(self, value):
        self.queue.append(value)  # Way to add items to the end

    def dequeue(self):
        if len(self.queue) != 0:  # If it's not empty
            return self.queue.pop(0)  # Remove the first item and return it
        return None  # All of these functions return None if there's nothing in the queue
    
    def front(self):
        if len(self.queue) != 0:
            return self.queue[0]  # Just returns the front
        return None
    
    def back(self):
        if len(self.queue) != 0:
            return self.queue[-1]  # Just returns the end
        return None

    def is_empty(self):
        """Function to check if the queue is empty easily (could be done with front(), but this makes readabilty better)"""
        return len(self.queue) == 0

class Vertex:
    """A class to represent our basic vertices of the graphs"""
    def __init__(self, name):
        # This is just a container to hold data
        self.name = name  # Holds a name
        self.color = "white"  # the color
        self.distance = float('inf')  # the distance for search
        self.previous = None  # The previous element
        self.finish = 0  # The time it finished (in a dfs)


class AdjacencyList:
    """A class to represent our graphs with built in methods for searching"""
    def __init__(self):
        self.vertices = {}  # Holds all the verticies as a dictonary based on string
        self.adjancencies = {}  # Holds all of the adjacencies
        self.time = 0  # The current time (used for dfs)

    def add_vertex(self, name):
        self.vertices[name] = Vertex(name)  # Adds a vertex with the passed in name to our list of vertices
        self.adjancencies[name] = []  # Adds the same vertex to our adjacencies dictonary but with no connections yet
    
    def add_adjacency(self, vertex_1, vertex_2):  # takes in names of two vertices and forms a unidirectional edge
        self.adjancencies[vertex_1].append(vertex_2)  # Adds vertex 2's name to the list of adjacencies for vertex 1
        self.adjancencies[vertex_2].append(vertex_1)  # The same but the other way around

    def add_dir_adjacency(self, vertex_1, vertex_2):  # takes in the names of two vertices and forms a directional edge (vertex_1 -> vertex_2)
        self.adjancencies[vertex_1].append(vertex_2)  # Adds vertex 2's name to the list of adjacencies for vertex 1

    def bfs(self, start):
        """Method that handles the breadth first search. Takes in the name of a vertex"""
        first_vertex = self.vertices[start]  # The given name is converted to its vertex object
        for vertex in self.vertices.values():  # Goes through each element
            if vertex is not first_vertex:  # If it's not the first element, reset it
                vertex.color = "white"
                vertex.distance = float('inf')
                vertex.previous = None
            else:  # If it's the first, set it to discovered
                vertex.color = "gray"
                vertex.distance = 0
                vertex.previous = None
        
        q = Queue()  # A variable to hold our queue of verticies
        q.enqueue(first_vertex)  # Queues the first vertex
        print(f"DISCOVERED {first_vertex.name} WITH DISTANCE {first_vertex.distance}")  # Prints the console to track progress
        while not q.is_empty():  # goes until the queue is empty
            u = q.dequeue()  # Unqueues the vertex we're working with
            for v in self.adjancencies[u.name]:  # Goes through each vertex that is adjacent to the current vertex
                vertex = self.vertices[v]  # Changes from string of name to actual vertex objects
                if vertex.color == "white":  # If they're undiscovered, discover them
                    vertex.color = "gray"
                    vertex.distance = u.distance + 1
                    vertex.previous = u
                    print(f"DISCOVERED {vertex.name} WITH DISTANCE {vertex.distance}") # Prints the console to track progress
                    q.enqueue(vertex)  # Queue the new undiscovered vertex
                u.color = "black"  # When it's done set color to black to show that the vertex is done
    
    def dfs(self):
        """Method that handles the depth-first search."""
        for v in self.vertices.keys():  # Goes through each vertex
            vertex = self.vertices[v]  # Turns the name into a vertex (looking back I could have just iterated through the .values())
            vertex.color = "white"  # Resets the vertices
            vertex.previous = None
        self.time = 0  # Sets the lists time to 0 (needed for tracking)
        for v in self.vertices.keys():  # Goes theough each vertex again (this is often going to do very little, but if there detached vertices it will loop when there's nowhere to go, but still vertices left)
            vertex = self.vertices[v]
            if vertex.color == "white":  # If the vertex is undiscovered
                self.dfs_visit(vertex)  # Visit that node
    
    def dfs_visit(self, vertex):
        """Helper method for dfs"""
        self.time = self.time + 1  # Since we're visiting, we up the time
        vertex.distance = self.time  # This is the discover time
        vertex.color = "gray"  # mark that we've visited
        for v in self.adjancencies[vertex.name]:  # Goes through each vertex the current vertex is adjacent to
            new_vertex = self.vertices[v]  # Turns the name into the vertex object
            if new_vertex.color == "white":
                new_vertex.previous = vertex
                self.dfs_visit(new_vertex)  # Recursively call the next vertex to visit
        self.time = self.time + 1  # Once we're done visiting, we're done with the vertex, which ups the time
        vertex.finish = self.time  # And we mark the finish time
        vertex.color = "black"

        
def assemble_graph_1():
    """Helper function to make the first graph"""
    my_list = AdjacencyList()
    my_list.add_vertex('r')
    my_list.add_vertex('s')
    my_list.add_vertex('t')
    my_list.add_vertex('u')
    my_list.add_vertex('v')
    my_list.add_vertex('w')
    my_list.add_vertex('x')
    my_list.add_vertex('y')
    my_list.add_vertex('z')

    my_list.add_adjacency('r', 's')
    my_list.add_adjacency('r', 't')
    my_list.add_adjacency('r', 'w')
    my_list.add_adjacency('s', 'u')
    my_list.add_adjacency('s', 'v')
    my_list.add_adjacency('t', 'u')
    my_list.add_adjacency('u', 'y')
    my_list.add_adjacency('y', 'v')
    my_list.add_adjacency('y', 'x')
    my_list.add_adjacency('v', 'w')
    my_list.add_adjacency('w', 'x')
    my_list.add_adjacency('w', 'z')
    my_list.add_adjacency('x', 'z')

    return my_list

def assemble_graph_2():
    """Helper function to make the second graph"""
    my_list = AdjacencyList()
    my_list.add_vertex('u')
    my_list.add_vertex('v')
    my_list.add_vertex('w')
    my_list.add_vertex('x')
    my_list.add_vertex('y')
    my_list.add_vertex('z')

    my_list.add_dir_adjacency('u', 'v')
    my_list.add_dir_adjacency('u', 'x')
    my_list.add_dir_adjacency('v', 'y')
    my_list.add_dir_adjacency('w', 'y')
    my_list.add_dir_adjacency('w', 'z')
    my_list.add_dir_adjacency('x', 'v')
    my_list.add_dir_adjacency('y', 'x')
    my_list.add_dir_adjacency('z', 'z')

    return my_list




def main():
    # Part 1 - BFS
    print("\nBFS Test Case\n")
    my_list = assemble_graph_1()  # Make the graph
    my_list.bfs('s')  # make the graph, starting on vertex s

    # Part 2 - DFS
    print("\nDFS Test Case (discover time/finish time)\n")
    my_second_list = assemble_graph_2()
    my_second_list.dfs()
    for vertex in my_second_list.vertices.values():  # Goes through each vertex
        print(str(vertex.name) + ": " + str(vertex.distance) + " / " + str(vertex.finish))  # Prints the details of the vertex



main()  # Start the program