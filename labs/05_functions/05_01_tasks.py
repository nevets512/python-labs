'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

def is_divisible_by_4_or_7():
    if (num % 4 == 0) or (num % 7 == 0):
        return True
    return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

def is_divisible_by_both():
    if (num % 4 == 0) and (num % 7 == 0):
        return True
    return False

# take in a number from the user between 1 and 1,000,000,000

num = int(input('Please enter a number between 1 and 1,000,000,000: '))


# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

x = (is_divisible_by_4_or_7())

y = (is_divisible_by_both())

# print your new variables to display the results

print(x)

print(y)

##not finished yet, need to fix to pass the user input as the arguments - see slack discussion with Johnny on 8/25/19





# num = 15
# divisible1 = 5
# divisible2 = 15
#
# def addition(x, y):
#     a = x + y
#     return a
#
# a = addition(5, 10)
# print(a)
#
#
# y = is_divisible_by() # y is assigned whatever the function returns
# #x = int(input("num: "))
#
# x = 1
#
#
#
# z = x + y
#
# print(z)



#print(is_divisible_by_4_or_7(29))




#def is_divisible():
#    a = int(input("first number: "))
#     b = int(input("second number: "))
#
#     if a % b == 0:
#         print("div as integers")
#     else:
#         print("not div as integers")
#
#
# is_divisible()





