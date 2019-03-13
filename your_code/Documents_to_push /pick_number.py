import sys

# Condition of the game (pick a number between 1 and 100) :

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
