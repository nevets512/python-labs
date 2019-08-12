'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

my_list = [1, 1, 1, 5, 5, 3, 5, 9, 4, 99, 0]

my_list = list(set(my_list))

print(my_list)
