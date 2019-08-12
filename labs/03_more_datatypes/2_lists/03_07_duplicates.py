'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

list_2 = []
for i in list_:
    if i not in list_2:
        list_2.append(i)

print(list_2)

