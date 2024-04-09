'''
Author: Michael Stang
Date: 03-28-24
Lab: lab 7
Last modified: 03-28-24
Purpose: Basic implementation of a Disjoint set
'''

class Node:
    # Node class to hold values and from trees
    def __init__(self, value):
        self.value = value  # Var to hold the value
        self.parent = None  # Var to hold this node's parent
        self.rank = 0  # Var to hold to rank
    def __repr__(self):
        return f"[NODE: (Value = {self.value}), Parent = {self.parent if self.parent != self else None}, Rank = {self.rank})]\n"  # A part for nice output

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

def main():
    my_disjoint_set = DistjointSet()  # Makes a Disjoint set for testing
    nodes = {"a": Node("a"), "b": Node("b"), "c": Node("c"), "d": Node("d"), "e": Node("e"), "f": Node("f"), "g": Node("g"), "h": Node("h")}  # List of nodes to add
    for node in nodes.values():  # Adds the nodes to the Disjoint Set
        my_disjoint_set.make_set(node)

    # Does the operations requested
    my_disjoint_set.union(nodes["b"], nodes["a"])
    my_disjoint_set.union(nodes["d"], nodes["c"])
    my_disjoint_set.union(nodes["f"], nodes["e"])
    my_disjoint_set.union(nodes["f"], nodes["g"])
    my_disjoint_set.union(nodes["c"], nodes["b"])
    my_disjoint_set.union(nodes["g"], nodes["h"])
    my_disjoint_set.union(nodes["d"], nodes["g"])
    my_disjoint_set.find_set(nodes["f"])
    
    # Prints the PARENT of each element
    print("PARENT ELEMENT FOR EACH ELEMENT")
    for node in nodes.values():
        print(f"parent({node.value}) -> {node.parent.value}")

    # Prints the RANK of each element
    print("\n\RANK FOR EACH ELEMENT")
    for node in nodes.values():
        print(f"rank({node.value}) -> {node.rank}")

main()