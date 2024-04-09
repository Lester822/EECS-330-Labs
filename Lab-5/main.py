"""
ASSIGNMENT_NAME: EECS 330 Lab 5
FUNCTION: Outputs two test cases of uses of the BinarySearchTree class
INPUTS: NONE
OUTPUTS: Various facts about two BSTs
AUTHOR_NAME: Michael Stang
COLLABORATORS: NONE
CREATION_DATE: 02/28/24
"""


class BinaryNode:
    """Class that represents a basic node that the BST will be made up of"""
    def __init__(self, entry):
        self.entry = entry  # The value the node holds
        self.parent = None  # The node's parent
        self.left = None  # The node's left child
        self.right = None  # The node's right child
    def __str__(self):
        return (f"/NODE: {self.entry}/")

class BinarySearchTree:
    """Class that implements the functionality of a Binary Search Tree"""
    def __init__(self):
        self.root = None
    
    def tree_insert(self, value):
        """Method for inserting new values into the BST"""
        if self.root == None:  # If the tree is currently empty
            self.root = BinaryNode(value)  # Set the root to a new node
        else:  # Otherwise
            self._rec_tree_insert(value, self.root)

    def _rec_tree_insert(self, value, cur_node):
        """Recursive backend for adding new values to the tree"""
        if value < cur_node.entry:  # If the value we're adding is smaller than the current node
            # Go left
            if cur_node.left == None:
                cur_node.left = BinaryNode(value)
                cur_node.left.parent = cur_node
            else:
                self._rec_tree_insert(value, cur_node.left)
        else:  # If if the value we're adding is larger or the equal to the current node
            # Go right
            if cur_node.right == None:
                cur_node.right = BinaryNode(value)
                cur_node.right.parent = cur_node
            else:
                self._rec_tree_insert(value, cur_node.right)
    
    def inorder_tree_walk(self, action=print):
        """Method to print the tree IN ORDER"""
        self._rec_inorder_tree_walk(self.root, action)  # Calls the recursive function backend for the functionality

    def _rec_inorder_tree_walk(self, cur_node, action):
        """Recursive function to implement tree walk"""
        if cur_node.left is not None:  # If the current node has a node on it's left...
            self._rec_inorder_tree_walk(cur_node.left, action)  # Go there
        action(f"{cur_node.entry}", end=" ")
        if cur_node.right is not None:  # If the current node has a node it's right...
            self._rec_inorder_tree_walk(cur_node.right, action)  # Go there

    def tree_search(self, search_value):
        """Front facing function to search for a node within the BST"""
        return self._rec_tree_search(search_value, self.root)

    def _rec_tree_search(self, search_value, cur_node):
        """Back end recursive function to search for a node within the BST"""
        if cur_node is None:  # Base case where the value is NOT in the BSt
            return None
        elif cur_node.entry == search_value:  # Base case where we find the value
            return cur_node
        elif search_value < cur_node.entry:  # If the value is smaller than our current value
            return self._rec_tree_search(search_value, cur_node.left)  # Go left
        else:  # If the value is larger than our current value
            return self._rec_tree_search(search_value, cur_node.right)  # Go right
    
    def tree_minimum(self, start_node=None):
        """Method for finding the smallest keyed node in the BST"""
        if self.root is None:  # Checks for the base case that there are no values in the tree
            return None
        if start_node == None:
            cur_node = self.root  # Sets a var to hold what node we're working with
        else:
            cur_node = start_node
        while cur_node.left is not None:  # As long as there is another node left of our current node, we continue
            cur_node = cur_node.left
        return cur_node   # Once there are no more nodes to the left, we're at the smallest value

    def tree_maximum(self, start_node=None):
        """Method for finding the smallest keyed node in the BST"""
        if self.root is None:  # Checks for the base case that there are no values in the tree
            return None
        if start_node == None:
            cur_node = self.root  # Sets a var to hold what node we're working with
        else:
            cur_node = start_node
        while cur_node.right is not None:  # As long as there is another node left of our current node, we continue
            cur_node = cur_node.right
        return cur_node   # Once there are no more nodes to the left, we're at the smallest value

    def tree_successor(self, node):
        """Function to find the next node in a tree if walked IN ORDER"""
        if node.right is not None:  # Makes sure there is somewhere to go right
            return self.tree_minimum(node.right)  # Finds the left most right node
        else:
            parent = node.parent  # Gets the parent of the node
            while parent is not None and node == parent.right:  # Moves right
                node = parent  # Moves upwards
                parent = parent.parent  # Moves upwards
            return parent  # Returns the final node that is the successor
    
    def tree_predecessor(self, node):
        """Function to find the previous node in a tree if walked IN ORDER"""
        if node.left is not None:  # Makes sure there is somewhere to go left
            return self.tree_maximum(node.left)  # Finds the rightmost left subtree
        else:
            parent = node.parent  # Same logic as successor but left and up
            while parent is not None and node == parent.left:
                node = parent
                parent = parent.parent
            return parent

def main():
    """Function to handle the test cases for the classes implemented"""
    
    # TEST CASE 1
    print("\nTEST CASE 1\n")
    test_case_1_numbers = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]  # List of numbers to be added to the tree
    test_case_1_tree = BinarySearchTree()
    for item in test_case_1_numbers:  # Loops to add items to the tree
        test_case_1_tree.tree_insert(item)
    print("In Order Print: ", end="")
    test_case_1_tree.inorder_tree_walk()  # Handles printing
    print(f"\nTree Minimum: {test_case_1_tree.tree_minimum().entry}")  # Various formatted strings to handle nice output
    print(f"Tree Maximum: {test_case_1_tree.tree_maximum().entry}")
    print(f"13's Successor: {test_case_1_tree.tree_successor(test_case_1_tree.tree_search(13)).entry}")

    # TEST CASE 2 (pretty much the same as above, but with different numbers)

    print("\n\nTEST CASE 2\n")
    test_case_2_numbers = [37, 24, 51, 7, 32, 41, 85, 2, 40, 120]
    test_case_2_tree = BinarySearchTree()
    for item in test_case_2_numbers:
        test_case_2_tree.tree_insert(item)
    print("In Order Print: ", end="")
    test_case_2_tree.inorder_tree_walk()
    print(f"\nTree Minimum: {test_case_2_tree.tree_minimum().entry}")
    print(f"Tree Maximum: {test_case_2_tree.tree_maximum().entry}")
    print(f"40's Predecessor: {test_case_2_tree.tree_predecessor(test_case_2_tree.tree_search(40)).entry}")  # This is now predeccesor instead of successor

main()  # Starts the program