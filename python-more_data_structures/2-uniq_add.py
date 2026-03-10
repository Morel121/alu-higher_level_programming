#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).
    
    Args:
        my_list: The initial list containing possible duplicates.
        
    Returns:
        The sum of the unique integers.
    """
    # 1. Convert the list to a set to remove duplicates
    unique_numbers = set(my_list)
    
    # 2. Sum the elements of the set and return the result
    return sum(unique_numbers)
