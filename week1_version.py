# getting input from player
import random

guess = 10101010

THE_NUMBER = 2

while guess != THE_NUMBER:

    range_of_guess = int(input('Please input a range: '))

    lower = 0
    upper = range_of_guess

    THE_NUMBER = random.randint(lower, upper)

    # --------------------------------------------------------------------
    # determining the no of guess allowed

    if range_of_guess <= 100:

        # no_of_guess = 3

        print('\nOkay you have 3 chances. Go ahead')
        iterator = iter([1, 2, 3])

    else:

        # no_of_guess = 5

        print("\nNow you have 5 chances. ")
        iterator = iter([1, 2, 3, 4, 5])

    # --------------------------------------------------------------------
    # getting input from player

    for i in iterator:

        guess = int(input('\nMake a guess: '))

        # --------------------------------------------------------------------
        # retry when it is out of range

        if guess < lower or guess > upper:
            guess = int(input('\nThe number is out of range. Please input another number.'))

        # --------------------------------------------------------------------
        # comparing and resetting the boundary for each guess

        new_boundary = guess

        if guess < THE_NUMBER:

            lower = new_boundary

            print(f'\nNope. Now guess between {lower} and {upper}')



        elif guess > THE_NUMBER:

            upper = new_boundary

            print(f'\nNope. Now guess between {lower} and {upper}')



        elif guess == THE_NUMBER:
            print('\nCongratulations! You got it')

    if guess != THE_NUMBER:
        print(f"You wish. The number is {THE_NUMBER}. Game Over.")

    # --------------------------------------------------------------------
    # conintue or not

    x = input('Do you want to continue? (yes/no) ')

    if x == 'yes' and guess == THE_NUMBER:
        guess += 1

    if x == 'no' and guess != THE_NUMBER:
        guess = THE_NUMBER

