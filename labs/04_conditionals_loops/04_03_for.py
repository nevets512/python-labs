'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

my_list = list(range(1, 101))

for num in my_list:
    if num % 2 != 0:
        print(num, end=" ")

