#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows.

    Returns:
        list: A list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        # Start the new row with 1
        curr_row = [1]
        
        # Calculate the middle elements
        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])
            
        # End the new row with 1
        curr_row.append(1)
        triangle.append(curr_row)

    return triangle
