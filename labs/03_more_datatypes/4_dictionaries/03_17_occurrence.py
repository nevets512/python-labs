'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

my_str = input("Please enter a string: ")

my_dict = {}

for x in my_str:
    my_dict[x] = my_dict.get(x, 0) + 1

print(my_dict)



