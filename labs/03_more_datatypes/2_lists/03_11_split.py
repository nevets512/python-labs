'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

sentence_1 = input("Please enter a sentence: ")

def Convert(string):
    li = list(string.split())
    return li

print(Convert(sentence_1))


# Python program to check if two
# to get unique values from list
# using traversal

# function to get unique values
def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
        # print list
    for x in unique_list:
        print
        x,

    # driver code


list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)

list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique values from 2nd list is")
unique(list2)



