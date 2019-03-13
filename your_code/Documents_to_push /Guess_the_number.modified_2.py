#!/usr/bin/env python
# coding: utf-8

#

import random

import pick_number


# Define the rules of the game:


def guess_the_number():
    
    number_of_guesses_left = 8

    # choose number and set the condition to play the game:
    
    your_number = pick_number.condition_to_play_the_game()

    # random function creates a random number between 1 and 100 to be picked in order to win:
        
    random_number = random.randint(1,100)

    if your_number == random_number:

        print("YOU WIN WITH FIRST TRY, OMG!!")

 
    while your_number != random_number:

        if your_number > random_number:

            number_of_guesses_left -= 1

            print(f' Your number of guesses left is {number_of_guesses_left}')
            
            # ask the player to choose a higher number:

            your_number = pick_number.condition_to_play_the_game("Choose lower number. Your number is ")

            # if the number of guesses left reaches 0, break the while loop 
            # and player loses the game
        
            if number_of_guesses_left == 0:

                break


        elif your_number < random_number:

            number_of_guesses_left -= 1

            print(f' Your number of guesses left is {number_of_guesses_left}')
            
            # ask the player to choose a higher number:

            your_number = pick_number.condition_to_play_the_game("Choose higher number. Your number is ")

            # if the number of guesses left reaches 0, break the while loop 
            # and player loses the game
            
            if number_of_guesses_left == 0:

                break

        elif your_number == random_number:

            print("You win!")


    # Condition to lose:

    if number_of_guesses_left == 0:

        print("YOU LOSE!")

        print(f' The random number was {random_number}')
        
        # if the players loses, the game restarts: 

        guess_the_number()


    # Condition to win:

    if number_of_guesses_left > 0:

        print("YOU WIN!")

    print(f' The random number was {random_number}')



# Execute the game:

guess_the_number()


# Possible improvements:

# add choice of range
# add level of difficulty

