'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

def custom_sort(t):
    return t[1]


L = [("Alice", 25), ("Bob", 20), ("Alex", 5)]
L.sort(key=custom_sort)
print(L)

