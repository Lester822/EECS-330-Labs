"""
ASSIGNMENT_NAME: EECS 330 Lab 4
FUNCTION: Outputs two lists before and after being sorted
INPUTS: NONE
OUTPUTS: 2 Sorted Lists
AUTHOR_NAME: Michael Stang
COLLABORATORS: NONE
CREATION_DATE: 02/20/24
"""


class MaxHeap:
    def __init__(self):
        '''Initilization of the MaxHeap class including making the list that makes up the heap'''
        self._root = []

    def add(self, add):
        '''Add a new value to the heap'''
        self._root.append(add)  # Adds the new value to the end of our list

        self._upheap(len(self._root) - 1)  # Upheaps the last element in the heap to get it into the correct position
    
    def _upheap(self, index):
        '''Upheap the element at the given index'''
        if index == 0:  # The base case of our recursion
            pass
        elif self._root[(index-1)//2] < self._root[index]:  # Checks if the parent of our cvalue is smaller, and if it is...
            temp = self._root[((index-1)//2)]  # Swaps them
            self._root[(index-1)//2] = self._root[index]
            self._root[index] = temp
            self._upheap((index-1)//2)  # Calls the function recursively
    
    def remove(self):
        '''Remove the root element from the heap'''
        if len(self._root) == 0:  # Checks if we're trying to remove the top element of an empty heap
            raise Exception("Heap is empty")
        elif len(self._root) == 1:  # If the heap is just 1 element, the heap is now empty
            self._root = []
        else:  # Otherwise
            self._root[0] = self._root[len(self._root) - 1]  # We take the last element in our heap and move it to the front
            self._root.pop(len(self._root) - 1)  # Remove the last element from the heap
            self._downheap(0)  # Then call downheap to fix the heap

    def _downheap(self, index):
        '''Downheap the element at the given index'''
        heap_size = len(self._root)
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        # Check if left child exists and is greater than the current largest
        if left_child_index < heap_size and self._root[left_child_index] > self._root[largest]:
            largest = left_child_index

        # Check if right child exists and is greater than the current largest
        if right_child_index < heap_size and self._root[right_child_index] > self._root[largest]:
            largest = right_child_index

        # If the largest element is not the current element, swap them
        if largest != index:
            self._root[index], self._root[largest] = self._root[largest], self._root[index]
            # Recursively heapify the affected sub-tree
            self._downheap(largest)
        
    def peek(self):
        '''Return the top element of the heap'''
        if len(self._root) == 0: # Checks if the heap is empty
            raise Exception("Heap is empty")
        return self._root[0]
        
    def __str__(self): 
        '''Overloaded STR method to act like a list'''
        return str(self._root)
        
    def __len__(self): 
        '''Overloaded len() function to act like a list'''
        return len(self._root)

def make_max_heap(input_list):
    '''Take in a list and output a MaxHeap with those elements'''
    my_heap = MaxHeap()  # Our MaxHeap to store values in
    for entry in input_list:  # Goes through each element in the list
        my_heap.add(entry)  # Adds it to the heap
    return my_heap  # Returns our newly created heap

def heapsort(input_list):
    heap = make_max_heap(input_list)  # Get our heap from the list
    
    sorted_list = []  # Create a new list to store our newly sorted list

    while len(heap) > 0:  # While there is still something in the heap
        max_element = heap.peek()  # Get the top of the heap
        sorted_list.insert(0, max_element)  # Add that to the front of the sorted list (would be back of list if it was a MinHeap)
        heap.remove()  # Get rid of the top element of the heap

    return sorted_list  # Return our new list


def main():
    '''Runs the program'''
    
    # First Test Case
    print("\nTEST CASE 1\n")
    first_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(f"Initial List: {first_list}")
    sorted_first_list = heapsort(first_list)
    print(f"Sorted List: {sorted_first_list}")

    # Second Test Case
    print("\n\nTEST CASE 2\n")
    second_list = [10, 3, 12, 100, 78, 34, 4, 5, 9000, -4, 67, 88, 99, 111, 222]
    print(f"Initial List: {second_list}")
    sorted_second_list = heapsort(second_list)
    print(f"Sorted List: {sorted_second_list}")


main()