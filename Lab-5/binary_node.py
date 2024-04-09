'''
Author: Michael Stang
Date: 04-21-2023
Last modified: 04-02-2023
Purpose: Basic class for a Binary Node
'''

class BinaryNode:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None