'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

sentence_1 = (input("Please enter a sentence: "))

x = (sentence_1.split())

print(x)
print(type(x))

list_of_tuples = []

print(type(list_of_tuples))

for i in x:
    list_of_tuples.append(tuple(i[0:]))

print(list_of_tuples)
print(type(list_of_tuples))




