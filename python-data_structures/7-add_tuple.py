#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements with padding of 0
    # and only use the first 2 elements if they are longer.
    # We can achieve this by extending with (0, 0) and then slicing the first 2 elements.
    adj_a = (tuple_a + (0, 0))[:2]
    adj_b = (tuple_b + (0, 0))[:2]

    # Perform element-wise addition
    result_tuple = (adj_a[0] + adj_b[0], adj_a[1] + adj_b[1])
    return result_tuple
