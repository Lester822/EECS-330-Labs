'''
Author: Michael Stang
Date: 03-21-24
Lab: lab 6
Last modified: 03-21-24
Purpose: Basic implementation of a hash table using double hashing
'''

class HashTable:  # Class that represents our hash table
    
    def __init__(self, length):
        self._length = length  # The length of the hashtable
        self._table = []  # Var to hold the values of the hashtable
        for i in range(length):  # Makes the list inside the hash table the right length, filling in "NIL"
            self._table.append("NIL")
    
    def length(self):
        return self._length  # A function to get the length rather than pulling it directly

    def table(self):
        return self._table

    def hash_insert(self, element, hash_function):
        """Insert a value into the hashtable using the passed-in hash function"""
        index = 0  # Index to track iteration
        while index != self._length-1:  # As long as we aren't at the end
            pos = hash_function(element, index, self._length)  # Calculate which position to try and insert based on passed in hash-fuction
            if self._table[pos] == "NIL":  # If it's empty
                self._table[pos] = element  # Set the value in that postition
                return pos  # Return the position so the user can know where it was put
            else:
                index += 1  # Otherwise, if it wasn't empty, repeat...
        raise Exception("Hashtable overflow")  # If every slot is full, error

    def hash_search(self, element, hash_function):
        """Function that searched for an element based on a given hash function"""
        index = 0  # Index to hold iteration
        pos = 0
        while self._table[pos] != "NIL" or index != self._length-1:  # Repeats until we've found the element
            pos = hash_function(element, index, self._length)  # Gets the next pos to check
            if self._table[pos] == element:  # If the element is there
                return pos  # Return that position
            index += 1  # Otherwise, iterate
        return "NIL"  # If none are found, return "NIL"

def double_hash(element, index, length, hash_one, hash_two):
    """Basic function that does a double hash given two individual hashes"""
    return (hash_one(element) + (index * hash_two(element))) % length

def hash_one(element):
    """The hash function described in the first example"""
    return element % 13

def hash_two(element):
    """The second hash function described in the first example"""
    return 1 + (element % 11)

def hash_three(element):
    """The first hash function described in the second example"""
    return element % 7

def hash_four(element):
    """The second hash function described in the second example"""
    return 5-(element % 5)

def prob_1_hash(element, index, length):
    """A hash function specialized for example 1"""
    return double_hash(element, index, length, hash_one, hash_two)

def prob_2_hash(element, index, length):
    """A hash function sepcialized for example 2"""
    return double_hash(element, index, length, hash_three, hash_four)

def main():
    print("\nHASHTABLE 1\n")  # Header
    hashtable_1 = HashTable(13)  # Makes an empty hash table
    elements_1 = [79, 69, 72, 50, 98, 14]  # List of elements to add
    for elem in elements_1:
        hashtable_1.hash_insert(elem, prob_1_hash)  # Adds them all using the hash function
    print("Hashtable After Inserts: ", hashtable_1.table())  # Prints the table
    print("Search For 14: ", hashtable_1.hash_search(14, prob_1_hash))  # Prints the results of a hash search
    print("Search For 66: ", hashtable_1.hash_search(66, prob_1_hash))  # Prints the results of a hash search


    # ALL CODE BELOW IS THE SAME AS ABOVE, BUT WITH DIFFERNET NUMBERS (AS GIVEN IN EXAMPLE 2)
    print("\nHASHTABLE 2\n")
    hashtable_2 = HashTable(13)
    elements_2 = [10, 82, 40, 35, 15, 21, 52]
    for elem in elements_2:
        hashtable_2.hash_insert(elem, prob_2_hash)
    print("Hashtable After Inserts: ", hashtable_2.table())
    print("Search For 52: ", hashtable_2.hash_search(52, prob_2_hash))
    print("Search For 11: ", hashtable_2.hash_search(11, prob_2_hash))

main()  # Starts the program