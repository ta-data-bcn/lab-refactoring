import random


# List of colors available and max number of tries for the game
options = ['blue', 'green', 'red', 'yellow', 'white', 'black']
tries = 10
number_colors = 4


# List of functions used
def machine_picks_colors():
    """
    The computer picks a random color-code from the ones available
    in the list 'options'.

    Returns:
      A list with the randomized 4-color-code.
    """
    code = random.choices(options, k=number_colors)
    print(f'Computer\'s randomized code is: {code}')
    return code


def player_picks_colors():
    """
    The function asks the player to pick a color-code and returns it.

    Returns:
      A list with the 4-color-code picked by the user.
    """
    colors = []
    while len(colors) < number_colors:
        choice = input(f"Choose one color from {options} and type it: ")
        if choice in options:
            colors.append(choice)
        else:
            print('Type a color:')
    print(f"You're code is: {colors}")
    return colors

# Step 1 of the game: the machine picks 4 colors.
machine_code = machine_picks_colors()

# Step 2 of the game: player picks 4 colors and plays.
for i in range(tries):

    person_guess = player_picks_colors()

    if person_guess == machine_code:
        print("You win!")
        break

    for i in range(len(person_guess)):
        if person_guess[i] == machine_code[i]:
            print(1)
        elif person_guess[i] in machine_code:
            print(0)
        else:
            print('-')

    tries -= 1
    print(f"You have {tries} tries left")

    if tries == 0:
        print(f"You lost. The code was {machine_code}")