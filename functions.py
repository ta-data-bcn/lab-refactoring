options = ['blue', 'green', 'red', 'yellow', 'white', 'black']

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