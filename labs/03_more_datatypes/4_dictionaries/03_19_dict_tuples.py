'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''

input_dict = {"item1": 5, "item2": 6, "item3": 1}

x = list(tuple(input_dict.items()))

def custom_sort(t):
    return t[1]


x.sort(key=custom_sort)
print(x)
