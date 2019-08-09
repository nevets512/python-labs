'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

sentence_1 = input("Please enter a sentence: ")

sentence_2 = input("Please enter a sentence: ")

sentence_3 = input("Please enter a sentence: ")

list = (sentence_1, sentence_2, sentence_3)

print(max(list, key = len))


