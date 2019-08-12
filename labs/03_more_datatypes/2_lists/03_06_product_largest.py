'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

numbers = list(map(int, input('Enter ten numbers separated by a space: ').split()))

print(max(numbers))

my_list = []

for i in range(1,10):
    my_list.append(i)

result = 1

for item in my_list:
    result = result * item

print(result)




