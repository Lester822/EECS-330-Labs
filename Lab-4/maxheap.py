'''
Author: Michael Stang
Date: 04-23-2023
Lab: lab09
Last modified: 04-23-2023
Purpose: A class to implement a list-based MAXHEAP
'''

class MaxHeap:
    def __init__(self):
        self._root = []

    def add(self, add):
        '''Add a new value to the heap'''
        self._root.append(add)

        self._upheap(len(self._root) - 1)  # Upheaps the last element in the heap
    
    def _upheap(self, index):
        '''Upheap the element at the given index'''
        if index == 0:
            pass
        elif self._root[(index-1)//2] < self._root[index]:
            temp = self._root[((index-1)//2)]
            self._root[(index-1)//2] = self._root[index]
            self._root[index] = temp
            self._upheap((index-1)//2)
    
    def remove(self):
        '''Remove the root element from the heap'''
        if len(self._root) == 0:
            raise Exception("Heap is empty")
        elif len(self._root) == 1:
            self._root = []
        else:
            self._root[0] = self._root[len(self._root) - 1]
            self._root.pop(len(self._root) - 1)
            self._downheap(0)

    def _downheap(self, index):
        '''Downheap the element at the given index'''
        try:
            if self._root[index] < self._root[(2 * index) + 1] or self._root[index] < self._root[(2 * index) + 2]:
                temp = self._root[index]
                if self._root[(2 * index) + 1] < self._root[(2 * index) + 2]:
                    self._root[index] = self._root[(2 * index) + 2]
                    self._root[(2 * index) + 2] = temp
                    self._downheap((2 * index) + 2)
                elif self._root[(2 * index + 1)] > self._root[(2 * index) + 2]:
                    self._root[index] = self._root[(2 * index) + 1]
                    self._root[(2 * index) + 1] = temp
                    self._downheap((2 * index) + 1)
                else:
                    if self._root[(2 * index) + 1].age < self._root[(2 * index) + 2].age:
                        self._root[index] = self._root[(2 * index) + 2]
                        self._root[(2 * index) + 2] = temp
                        self._downheap((2 * index) + 2)
                    elif self._root[(2 * index + 1)].age > self._root[(2 * index) + 2].age:
                        self._root[index] = self._root[(2 * index) + 1]
                        self._root[(2 * index) + 1] = temp
                        self._downheap((2 * index) + 1)
                    else:
                        if self._root[(2 * index) + 1].arrival > self._root[(2 * index) + 2].arrival:
                            self._root[index] = self._root[(2 * index) + 2]
                            self._root[(2 * index) + 2] = temp
                            self._downheap((2 * index) + 2)
                        elif self._root[(2 * index + 1)].arrival < self._root[(2 * index) + 2].arrival:
                            self._root[index] = self._root[(2 * index) + 1]
                            self._root[(2 * index) + 1] = temp
                            self._downheap((2 * index) + 1)
        except IndexError:
            pass
    
    def peek(self):
        if len(self._root) == 0:
            raise Exception("Heap is empty")
        return self._root[0]
    
    def __str__(self):
        return str(self._root)
    
    def __len__(self):
        return len(self._root)