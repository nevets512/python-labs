'''
Code a game of rock paper scissors.

'''


# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper

    # for example if the variable hand is 0, it should return the string "scissor"
    pass

# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    pass



'''
Start here
'''
from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]

# take in a number 0-2 from the user that represents their hand

# generate a random number 0-2 to use for the computer's hand

# call the function get_hand to get the string representation of the user's hand

# call the function get_hand to get the string representation of the computer's hand

# call the function determine_winner to figure out the winner

# print out the player hand and computer hand

# print out the winner