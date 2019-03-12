import random


def initialization():
    """Define the variables required for starting the game.

    :return:All the variables
    :rtype: int
    """
    guess_range = int(input('Please input a range: '))
    tries = rounds_of_guess(guess_range)
    lower_boundary = 0  # Lower boundary of guess
    upper_boundary = guess_range  # Upper boundary of guess initially equals to value of range
    gen_number = random.randint(lower_boundary, upper_boundary)  # Generate a random number in the range given
    finished = False  # Initially assigned False
    return finished, gen_number, lower_boundary, upper_boundary, tries, guess_range


def rounds_of_guess(guess_range):
    """Determining no. of rounds of guess based on the input from player

    :param guess_range: The range input by player
    :type guess_range: int
    :return: No. of rounds
    :rtype: int
    """
    if guess_range <= 100:
        rounds = 3  # Allow 3 rounds of guess
    else:
        rounds = 5  # Allow 5 rounds of guess
    print(f'\nNow you have {rounds} chances.')
    return rounds


def ask_guess(lower_boundary, upper_boundary):
    """Ask player for an input guess and check if it is in range

    :param lower_boundary: The lower boundary of the range within which the player make a guess
    :type lower_boundary: int
    :param upper_boundary: The upper boundary of the range within which the player make a guess
    :type upper_boundary: int
    :return: user_guess
    :rtype: int
    """
    player_guess = int(input('\nMake a guess: '))  # Ask for input from player
    while player_guess < lower_boundary or player_guess > upper_boundary:
        # When the guess is out of range, it asks players for a new input
        player_guess = int(input('\nThe number is out of range. Please input another number.'))
    return player_guess


def determine_new_boundary(guess_number,lower_boundary,upper_boundary,gen_number):
    """Compare input guess with current lower and upper boundary and update the range for next round

    :param guess_number: The number guessed by player
    :type guess_number: int
    :param lower_boundary: The lower boundary of the range within which the player make a guess
    :type lower_boundary: int
    :param upper_boundary: The upper boundary of the range within which the player make a guess
    :param gen_number: int
    :return: lower_boundary, upper_boundary
    :rtype: int
    """
    if guess_number < gen_number:
    # Redefining boundary
        lower_boundary = guess_number
        print(f'\nNope. Now guess between {lower_boundary} and {upper_boundary}')
    elif guess_number > gen_number:
        upper_boundary = guess_number
        print(f'\nNope. Now guess between {lower_boundary} and {upper_boundary}')
    return lower_boundary, upper_boundary
