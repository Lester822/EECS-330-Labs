from math import floor

def main():
    """Run the program"""
    
    # Insertion Sort
    print("\nINSERTION SORT:\n")
    first_list = [5, 2, 4, 6, 1, 3]  # The first list
    second_list = [12, 3, 4, 5, 101, 11, 2, 90, 45, 7, 80]  # The second list
    print(f"{first_list} -> ", end='')  # Prints to user what list is being sorted
    insertion_sort(first_list)
    print(f"{first_list}")  # Prints the final sorted list
    print(f"{second_list} -> ", end='')  # Prints to user what list is being sorted
    insertion_sort(second_list)
    print(f"{second_list}")  # Prints sorted list

    # Merge Sort
    print("\nMERGE SORT:\n")
    first_list = [12, 3, 7, 9, 14, 6, 11, 2]  # The first list
    second_list = [90, 80, 30, 40, 22, 3020, 1, 6, 9, 43, 99, 120, 456, 17, 26, 9001]  # The second list
    print(f"{first_list} -> ", end='')  # Prints to user what list is being sorted
    insertion_sort(first_list)
    print(f"{first_list}")  # Prints the final sorted list
    print(f"{second_list} -> ", end='')  # Prints to user what list is being sorted
    insertion_sort(second_list)
    print(f"{second_list}")  # Prints sorted list


def insertion_sort(input_list):
    size = len(input_list)  # Gets the size of the list
    for num in range(1, size):  # Loops a number of times equal to the length of the list
        key = input_list[num]  # Gets the current value
        j = num - 1  # Sets our counting variable to the index of our key
        while j >= 0 and input_list[j] > key:  # While we aren't at the start of the list and the num we're looking at is greater than the number we're putting in the list
            input_list[j+1] = input_list[j]  # Swap the numbers
            j = j - 1  # Then interate again
        input_list[j+1] = key  # sets the final position of the num we're looking at

def merge_sort(input_list, p, r):
    if p >= r:  # Checks if our p and r "pointers" have met
        return None  # if so, end
    q = floor((p+r)/2)  # calculates the mid point
    merge_sort(input_list, p, q)  # recursively calls merge_sort with the new divison
    merge_sort(input_list, q+1, r)  # resurveily does the other side too
    merge(input_list, p, q, r)  # Merges everything back together

def merge(input_list, p, q, r):
    """Merge two paritioned lists into a sorted list"""
    left_list = input_list[p:q+1]  # Makes a temp left list
    right_list = input_list[q+1:r+1]  # Makes a temp right list

    num = p  # A pointers for use
    i, j = 0, 0  # More pointers for use

    # Merge the left_list and right_list back into input_list
    while i < len(left_list) and j < len(right_list):  
        if left_list[i] <= right_list[j]:
            input_list[num] = left_list[i]
            i += 1
        else:
            input_list[num] = right_list[j]
            j += 1
        num += 1

    # Copy any remaining elements of left_list, if there are any
    while i < len(left_list):
        input_list[num] = left_list[i]
        i += 1
        num += 1

    # Copy any remaining elements of right_list, if there are any
    while j < len(right_list):
        input_list[num] = right_list[j]
        j += 1
        num += 1




main()