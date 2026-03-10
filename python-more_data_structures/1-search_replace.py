#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    
    Args:
        my_list: The initial list.
        search: The element to replace in the list.
        replace: The new element.
        
    Returns:
        A new list with the elements replaced.
    """
    # We use a list comprehension to create a new list.
    # For each element 'x', if it matches 'search', we use 'replace'.
    # Otherwise, we keep the original element 'x'.
    return [replace if x == search else x for x in my_list]
