#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    
    Args:
        matrix: A 2D array (list of lists) of integers.
        
    Returns:
        A new matrix of the same size with each value squared.
    """
    # We use a nested list comprehension to create a brand new matrix.
    # This ensures the original matrix remains unmodified.
    return [[item**2 for item in row] for row in matrix]
