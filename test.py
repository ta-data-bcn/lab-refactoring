options = ['blue', 'green', 'red', 'yellow', 'white', 'black']

def player_picks_colors():

    colors = []
    while len(colors) < 4:
        choice = input(f"Choose one color from {options} and type it (position {len(colors)+1})")
        if choice in options:
            colors.append(choice)
        else:
            print('Type a color:')
    print(f"You're code is: {colors}")
    return colors

player_picks_colors()