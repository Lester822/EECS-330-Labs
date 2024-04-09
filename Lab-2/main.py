"""
ASSIGNMENT_NAME: EECS 330 Lab 2
FUNCTION: Prints various results of binary searches and matrix mulitiplication
INPUTS: NONE
OUTPUTS: Various indicies and matricies
AUTHOR_NAME: Michael Stang
COLLABORATORS: The powerpoint slides for help with conceptually understanding whats happening
CREATION_DATE: 2/9/24
"""

from math import floor

def print_matrix(matrix):
    """Print a matrix to console in a nicer format"""
    for i in range(len(matrix)):  # Loops through each row of the matrix
        print(f"{matrix[i]} ")  # Prints that row

def binary_search(input_list, target, low_index, high_index):
    """Return the index of the target element in a passed in pre-sorted list"""
    if low_index > high_index:  # Checks to ensure that the low_index bounds of what we're checking isn't above the high_index (which would cause a recursion issue)
        return None 
    midpoint_index = floor(((low_index + high_index) / 2))  # Calculates the midpoint_index point between the high_index and low_index bounds
    if target == input_list[midpoint_index]:  # If the value we're looking at is the thing we're looking for
        return midpoint_index  # Return it
    elif target > input_list[midpoint_index]:  # Otherwise, we calculate if our value is larger or smaller and figure out which half of the list to check
        return binary_search(input_list, target, midpoint_index+1, high_index)  # Calls the function towards the right (greater values), forming recursion
    else:
        return binary_search(input_list, target, low_index, midpoint_index-1)  # Calls the function towards the left (lesser values)

    
def matrix_multiply(matrix_a, matrix_b, matrix_c, row_a, col_a, row_b, col_b, row_c, col_c, n):
    # Handles our reursive base case
    if n == 1:
        matrix_c[row_c][col_c] += matrix_a[row_a][col_a] * matrix_b[row_b][col_b]
        return
    
    # If we're not at our base case, we do recursion
    half = n // 2
    
    # Upper left quadrant
    matrix_multiply(matrix_a, matrix_b, matrix_c, row_a, col_a, row_b, col_b, row_c, col_c, half)  # Calls itself, but with half n
    matrix_multiply(matrix_a, matrix_b, matrix_c, row_a, col_a + half, row_b + half, col_b, row_c, col_c, half)  # Calls itself, but displaced and with half n
    
    # Does the same with the other quadrents

    # Upper right
    matrix_multiply(matrix_a, matrix_b, matrix_c, row_a, col_a, row_b, col_b + half, row_c, col_c + half, half)
    matrix_multiply(matrix_a, matrix_b, matrix_c, row_a, col_a + half, row_b + half, col_b + half, row_c, col_c + half, half)
    
    # Bottom left
    matrix_multiply(matrix_a, matrix_b, matrix_c, row_a + half, col_a, row_b, col_b, row_c + half, col_c, half)
    matrix_multiply(matrix_a, matrix_b, matrix_c, row_a + half, col_a + half, row_b + half, col_b, row_c + half, col_c, half)
    
    # Bottom right
    matrix_multiply(matrix_a, matrix_b, matrix_c, row_a + half, col_a, row_b, col_b + half, row_c + half, col_c + half, half)
    matrix_multiply(matrix_a, matrix_b, matrix_c, row_a + half, col_a + half, row_b + half, col_b + half, row_c + half, col_c + half, half)

def main():
    """Main function that runs the program"""
    print("\nBINARY SEARCH TEST CASES: \n")  # Header for the whole program

    # First Test Case For Binary Search
    print("\nTest 1: \n")  # Header for the search portion
    first_list = [3, 5, 7, 8, 9, 12, 15]
    number_to_search_1 = 15  # The number we are looking for
    print(f"List Being Searched: {first_list}\nNumber Being Searched For: {number_to_search_1}")  # Various prints to make formatting look decent
    first_location = (binary_search(first_list, number_to_search_1, 0, len(first_list)-1))
    print(f"Index Found At: {first_location}")

    # Second Test Case For Binary Search

    print("\nTest 2: \n")  # Same as above, but with a new list and new target
    second_list = [0, 2, 3, 7, 8, 9, 11, 56, 89, 100]
    number_to_search_2 = 56
    print(f"List Being Searched: {second_list}\nNumber Being Searched For: {number_to_search_2}")   # Various prints to make formatting look decent
    second_location = (binary_search(second_list, number_to_search_2, 0, len(second_list)-1))
    print(f"Index Found At: {second_location}")

    # First Test Case For Matrix Multiplication

    print("\n\nMATRIX MULTIPLICATION TEST CASES\n")  # Header for the matrix portion

    matrix_1a = [  # This is how we will represent matricies, with a list of lists, nicely displayed like this within the code to be readible
        [5,2,6,1],
        [0,6,2,0],
        [3,8,1,4],
        [1,8,5,6]
    ]

    matrix_1b = [
        [7,5,8,0],
        [1,8,2,6],
        [9,4,3,8],
        [5,3,7,9]
    ]

    end_matrix1 = [  # Final matrix to hold the final result
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]]  

    print("\nTest 1\n")  # Formatting for headers and outputs to make it look decent
    print_matrix(matrix_1a)
    print("\n" + " " * 4 + "X" + "\n")
    print_matrix(matrix_1b)
    print("\n" + " " * 4 + "=" + "\n")
    matrix_multiply(matrix_1a, matrix_1b, end_matrix1, 0, 0, 0, 0, 0, 0, len(matrix_1a))
    print_matrix(end_matrix1)

    matrix_2a = [  # Same as above but with a giant matrix
    [7, 9, 9, 7, 9, 3, 2, 5, 2, 8, 4, 4, 2, 6, 7, 5],
    [3, 4, 8, 9, 9, 1, 5, 6, 3, 5, 9, 3, 8, 3, 1, 3],
    [3, 5, 4, 2, 9, 3, 5, 8, 6, 9, 2, 2, 3, 9, 8, 5],
    [7, 7, 5, 7, 7, 4, 8, 1, 5, 9, 1, 4, 8, 5, 3, 4],
    [8, 6, 0, 9, 4, 1, 5, 0, 2, 1, 9, 7, 1, 6, 9, 0],
    [3, 9, 2, 9, 1, 3, 9, 6, 3, 2, 3, 2, 0, 9, 2, 3],
    [8, 6, 1, 2, 7, 5, 6, 7, 0, 1, 5, 9, 1, 2, 2, 1],
    [2, 9, 7, 6, 5, 6, 2, 4, 9, 1, 8, 4, 3, 3, 2, 7],
    [5, 9, 7, 3, 5, 9, 4, 7, 6, 7, 0, 4, 4, 5, 0, 2],
    [3, 0, 6, 7, 8, 9, 1, 6, 9, 5, 2, 3, 1, 7, 0, 6],
    [4, 3, 4, 7, 8, 9, 4, 0, 6, 0, 6, 3, 4, 3, 8, 9],
    [0, 3, 9, 2, 8, 8, 7, 2, 7, 5, 6, 3, 2, 9, 5, 8],
    [0, 3, 9, 0, 2, 0, 2, 0, 5, 2, 8, 5, 9, 6, 0, 0],
    [3, 3, 0, 8, 8, 7, 6, 2, 8, 4, 2, 0, 4, 0, 8, 7],
    [6, 3, 6, 5, 3, 0, 5, 6, 4, 8, 1, 6, 9, 2, 9, 3],
    [9, 1, 7, 9, 9, 2, 5, 8, 7, 6, 3, 4, 6, 9, 6, 5]
    ]
    
    matrix_2b = [  # The identity matrix, which when multiplied should result in the first matrix
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ]

    end_matrix2 = [  # The matrix to hold the final answer
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


    print("\nTest 2\n")  # Various prints for nice formatting
    print_matrix(matrix_2a)
    print("\n" + " " * 10 + "X" + "\n")
    print_matrix(matrix_2b)
    print("\n" + " " * 10 + "=" + "\n")
    matrix_multiply(matrix_2a, matrix_2b, end_matrix2, 0, 0, 0, 0, 0, 0, len(matrix_2a))
    print_matrix(end_matrix2)

main()

