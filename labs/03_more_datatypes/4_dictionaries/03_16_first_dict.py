'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

d = {}

d['name'] = 'Johnny'

print(d)

d['surname'] = "Jones"

print(d)

my_dict = {}

for i in range(1, 11):
    my_dict[i] = i + 10

print(my_dict)
my_dict[1] = 100

print(my_dict)

for k,v in my_dict.items():
    print(k,v)



