#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = []
    i = 0

    for item in my_list:
        if i != idx:
            new_list.append(item)
        i += 1

    return new_list
