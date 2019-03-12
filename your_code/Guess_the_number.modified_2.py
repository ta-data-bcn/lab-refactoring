#!/usr/bin/env python
# coding: utf-8

#


import random

import sys


# First condition of the game (pick a number between 1 and 100) :

def condition_to_play_the_game(string="Choose any integer between 1 and 100. Your number is "):

    your_number = input(string)

    # first we want to ensure that the user inputs an integer less than 100
    # otherwise exit the game:

    if your_number.isdigit():

        your_number = int(your_number)

        if your_number > 100:

            print('Your number exceeds 100. Please play again. ')

            sys.exit(1)

        print(" Your number is an integer and we can continue! ")

        return your_number

    else:

        print("You have not entered an integer. Please play again.  ")
        sys.exit(1)


# Define the rules of the game:

def guess_the_number():
    
    Number_of_guesses_left = 8

    # choose number and set the condition to play the game as detailed above:
    
    your_number = condition_to_play_the_game()

    # random function creates a random number between 1 and 100 to be picked in order to win:
        
    random_number = random.randint(1,100)

    if your_number == random_number:

        print("YOU WIN WITH FIRST TRY, OMG!!")

 
    while your_number != random_number:

        if your_number > random_number:
            
            # subtract one from number of guesses:

            Number_of_guesses_left -= 1

            print(f' Your number of guesses left is {Number_of_guesses_left}')
            
            # ask the player to choose a higher number:

            your_number = condition_to_play_the_game("Choose lower number. Your number is ")

            # if the number of guesses left reaches 0, break the while loop 
            # and player loses the game
        
            if Number_of_guesses_left == 0:

                break


        elif your_number < random_number:

            # subtract one from number of guesses:

            Number_of_guesses_left -= 1

            print(f' Your number of guesses left is {Number_of_guesses_left}')
            
            # ask the player to choose a higher number:

            your_number = condition_to_play_the_game("Choose higher number. Your number is ")

            # if the number of guesses left reaches 0, break the while loop 
            # and player loses the game
            
            if Number_of_guesses_left == 0:

                break

        elif your_number == random_number:

            print("You win!")


    # Condition to lose:

    if Number_of_guesses_left == 0:

        print("YOU LOSE!")

        print(f' The random number was {random_number}')
        
        # if the players loses, the game restarts: 

        guess_the_number()


    # Condition to win:

    if Number_of_guesses_left > 0:

        print("YOU WIN!")

    print(f' The random number was {random_number}')



# Execute the game:

guess_the_number()


# Possible improvements:

# add choice of range
# add level of difficulty

