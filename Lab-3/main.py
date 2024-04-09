import random

def partition(A, p, r):
    """Function that arranges lists and returns index of last swap"""
    x = A[r]  # The value of the end value stored as 'x'
    i = p - 1
    for j in range(p, r):  # Loops between the range we care about
        if A[j] <= x: # Checks if the value is smaller then are pivot point
            i = i + 1
            A[i], A[j] = A[j], A[i]  # Pythonic way to swap
    A[i+1], A[r] = A[r], A[i+1]  # Move pivot to correct position
    return i + 1

def randomized_partition(A, p, r):
    """Function that partitions using a randomly generated number"""
    i = random.randint(p, r)  # The randomly generated number
    A[r], A[i] = A[i], A[r]  # Swaps the 'r' index (the end) and the randomly generated index
    return partition(A, p, r)


def randomized_quicksort(A, p, r):
    """Function to start quick sorting"""
    if p < r:  # If the start point is before the end point
        q = randomized_partition(A, p, r)  # Gets partition
        randomized_quicksort(A, p, q-1)  # Recursively calls quicksort
        randomized_quicksort(A, q + 1, r)  # Recurisvely calls quicksort

def main():
    """Main runs the program's test cases"""
    list_one = [2, 1, 7, 8, 3, 5, 6, 4]  # First list to be sorted
    print(f"\nTEST CASE 1:\nList Pre-Sort: {list_one}")
    randomized_quicksort(list_one, 0, len(list_one)-1)  # Sorts here
    print(f"List Post-Sort: {list_one}")

    list_two = [60, 89, 90, 101, 500, 2, 0, 14, 34, 1000, 12, 67, 45, 44, 9000]  # Second list to be sorted
    print(f"\n\nTEST CASE 2:\nList Pre-Sort: {list_two}")
    randomized_quicksort(list_two, 0, len(list_two)-1)  # Sorts here
    print(f"List Post-Sort: {list_two}")

main()  # Starts the program