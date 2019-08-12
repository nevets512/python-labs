'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

num_1 = int(input("Enter a number between 1 and 1,000,000,000: "))

print(num_1)

num_2 = (num_1 / 3)

print(num_2)

num_2 = int(num_2)

if num_1 / num_2 == 3:
    print("YES, it's divisible by 3!!")
else:
    print("NO WAY MAN")
