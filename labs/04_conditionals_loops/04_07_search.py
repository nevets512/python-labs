'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

my_num = int(input("Please enter a number: "))

count = 0
while True:
    print(count)
    if count == my_num:
        break
    else:
        count += 1

print(count)

