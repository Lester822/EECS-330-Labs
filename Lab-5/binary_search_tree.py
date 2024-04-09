'''
Author: Michael Stang
Date: 04-21-2023
Last modified: 04-05-2023
Purpose: Basic class for BST
'''

from binary_node import BinaryNode

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.copy_tree = None

    def add(self, entry):
        '''Public method to add to BST'''
        if self.root == None:
            self.root = BinaryNode(entry)
        else:
            self.rec_add(entry, self.root)
    
    def rec_add(self, entry, cur_node):
        '''Recursivly moves through a BST to add new entries, not meant to be public facing'''
        if cur_node.entry == entry:  # This is the case where the entry is already in the tree, it simply does nothing
            raise ValueError(f"Value {entry} already in Binary Search Tree.")

        elif cur_node.entry > entry:
            if cur_node.left == None:
                cur_node.left = BinaryNode(entry)
            else:
                self.rec_add(entry, cur_node.left)
                
        elif cur_node.entry < entry:
            if cur_node.right == None:
                cur_node.right = BinaryNode(entry)
            else:
                self.rec_add(entry, cur_node.right)
    
    def search(self, target):
        '''Public facing returns item with given keyvalue'''
        search_result = self.rec_search(target, self.root)
        if search_result == False:
            raise Exception(f'Value {target} not found in BST.')
        else:
            return search_result
    
    def rec_search(self, target, cur_node):
        '''Recurvisly navigates tree to return target'''
        if cur_node == None:
            return False
        elif cur_node.entry == target:
            return cur_node.entry
        else:
            if cur_node.entry > target:
                return self.rec_search(target, cur_node.left)
            elif cur_node.entry < target:
                return self.rec_search(target, cur_node.right)

    def preorder_action(self, action):
        '''Does "action" on all nodes in tree in pre-order'''
        self.rec_preorder_action(self.root, action)

    def rec_preorder_action(self, cur_node, action):
        '''Recurive function that goes through all nodes and does action in pre-order'''
        action(cur_node.entry)
        if cur_node.left != None:
            self.rec_preorder_action(cur_node.left, action)
        if cur_node.right != None:
            self.rec_preorder_action(cur_node.right, action)

    def inorder_action(self, action):
        '''Does "action" on all nodes in tree in in-order'''
        self.rec_inorder_action(self.root, action)
    
    def rec_inorder_action(self, cur_node, action):
        '''Recurive function that goes through all nodes and does action in in-order'''
        if cur_node.left != None:
            self.rec_inorder_action(cur_node.left, action)
        action(cur_node.entry)
        if cur_node.right != None:
            self.rec_inorder_action(cur_node.right, action)

    def postorder_action(self, action):
        '''Does "action" on all nodes in tree in post-order'''
        self.rec_postorder_action(self.root, action)

    def rec_postorder_action(self, cur_node, action):
        '''Recurive function that goes through all nodes and does action in post-order'''
        if cur_node.left != None:
            self.rec_postorder_action(cur_node.left, action)
        if cur_node.right != None:
            self.rec_postorder_action(cur_node.right, action)
        action(cur_node.entry)
    
    def copy(self):
        '''Returns a copy of the BST'''
        if self.copy_tree == None:
            self.copy_tree = BinarySearchTree()
            self.preorder_action(self.copy_tree.add)
        else:
            raise Exception('Copy already exists')
    

    def remove(self, pokedex_number):
        '''Removes a node from the BST'''
        value = self.rec_remove_search(pokedex_number, self.root)
        if value == False:
            raise KeyError("Value not found in BST")
        else:
            target_node = value[0]
            prev_node = value[1]
            if prev_node == None: # if the target node is the root
                parent_dir = 'none'
            else:
                if prev_node.left == target_node:
                    parent_dir = 'left'
                else:
                    parent_dir = 'right'
            if target_node.left == None and target_node.right == None:  # if there are no children
                if parent_dir == 'left': # if the target node is the left child of the parent
                    prev_node.left = None
                if parent_dir == 'right':
                    prev_node.right = None
                else:
                    self.root = None
            elif (target_node.left != None and target_node.right == None): # if there is one LEFT child
                if parent_dir == 'left':
                    prev_node.left = target_node.left # set the parent's left child to the target's left child
                if parent_dir == 'right':
                    prev_node.right = target_node.left
                else:
                    self.root = target_node.left
            elif (target_node.left == None and target_node.right != None): # if there is one RIGHT child
                if parent_dir == 'left': # if the target node is the left child of the parent
                    prev_node.left = target_node.right 
                if parent_dir == 'right':
                    prev_node.right = target_node.right
                else:
                    self.root = target_node.right
            else: # there are two children
                if target_node.left.right == None: # if the left child has no right child
                    no_right = True
                biggest_left = self.rec_go_right(target_node.left)
                if parent_dir == 'left':
                    prev_node.left = biggest_left
                if parent_dir == 'right':
                    prev_node.right = biggest_left
                if parent_dir == 'none':
                    self.root = biggest_left
                biggest_left.right = target_node.right
                old_left = biggest_left.left
                biggest_left.left = target_node.left
                if no_right == True:
                    biggest_left.left.right = None
                else:
                    biggest_left.left.right = old_left
        
        
    def rec_remove_search(self, pokedex_number, cur_node, prev_node = None):
        '''Searches for node to remove'''
        if cur_node == None:
            return False
        elif cur_node.entry == pokedex_number:
            return cur_node, prev_node
        else:
            if cur_node.entry > pokedex_number:
                return self.rec_remove_search(pokedex_number, cur_node.left, cur_node)
            elif cur_node.entry < pokedex_number:
                return self.rec_remove_search(pokedex_number, cur_node.right, cur_node)
    
    def rec_go_right(self, cur_node):
        '''Returns the right most node in a BST'''
        if cur_node.right == None:
            return cur_node
        else:
            return self.rec_go_right(cur_node.right)
