import random
# importing random library to generate random number

guess_number = 3  # Number guessed by player
gen_number = 2  # Randomly generated number
guess_range = int(input('Please input a range: '))

def rounds_of_guess(guess_range):
    if guess_range <= 100:
        rounds = 3  # allow 3 rounds of guess
        print(f'\nOkay you have {rounds} chances. Go ahead')
        rounds_of_guess = [i for i in range(guess_range)]  # Create an iterator to run 3 rounds
    else:
        rounds = 5  # allow 5 rounds of guess
        print(f'\nNow you have {rounds} chances.')
        rounds_of_guess = [i for i in range(guess_range)]  # Create an iterator to run 5 rounds
    return rounds_of_guess

while guess_number != gen_number:
# Until a player make a correct guess, the following will keep executing


    lower_boundary = 0  # Lower boundary of guess
    upper_boundary = guess_range  # Upper boundary of guess initially equals to value of range

    gen_number = random.randint(lower_boundary, upper_boundary)


    for i in rounds_of_guess(guess_range):

        guess_number = int(input('\nMake a guess: '))

        # --------------------------------------------------------------------
        # retry when it is out of range

        if guess_number < lower_boundary or guess_number > upper_boundary:
            # When the guess is out of range, it asks players for a new input
            guess_number = int(input('\nThe number is out of range. Please input another number.'))

        # --------------------------------------------------------------------
        # comparing and resetting the boundary for each guess

        new_boundary = guess_number

        if guess_number < gen_number:
        # Redefining boundary
            lower_boundary = new_boundary
            print(f'\nNope. Now guess between {lower_boundary} and {upper_boundary}')
        elif guess_number > gen_number:
            upper_boundary = new_boundary
            print(f'\nNope. Now guess between {lower_boundary} and {upper_boundary}')
        elif guess_number == gen_number:
            print('\nCongratulations! You got it')

    if guess_number != gen_number:
        print(f"You wish. The number is {gen_number}. Game Over.")

    # --------------------------------------------------------------------
    # conintue or not

    choice = input('Do you want to continue? (yes/no) ')

    if choice == 'yes' and guess_number == gen_number:
        guess_number += 1

    if choice == 'no' and guess_number != gen_number:
        guess_number = gen_number

