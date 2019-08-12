'''
Print out every prime number between 1 and 100.

'''

my_list = list(range(1, 101))

for num in my_list:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

