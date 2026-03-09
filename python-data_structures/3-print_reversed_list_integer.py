#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    # Iterate through the list in reverse order using range
    # The range function can generate numbers in reverse order [2]
    # We start from the last index (length - 1), go down to index 0, stopping before -1
    for i in range(len(my_list) - 1, -1, -1):
        # Access the element at the current index
        number = my_list[i]
        # Use str.format() to print the integer
        # The format specifier 'd' is used for decimal integers
        print("{:d}".format(number))²
