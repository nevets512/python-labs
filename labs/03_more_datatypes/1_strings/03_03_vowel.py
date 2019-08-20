'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

sentence = input("Please enter a sentence: ")
vowel = input("Please enter a vowel: ")

print(sentence.count(vowel))
count = 0

for char in sentence:
    if char == vowel:
        count += 1

print(count)

