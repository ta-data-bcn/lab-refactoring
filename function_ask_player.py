# Define a function to ask the player to choose 4 colours between blue, green, orange, pink, red, yellow
def ask_player():
    """This function asks the player to choose 4 colours between blue, green, orange, pink, red, yellow
"""
    for i in range(len(computer)):
        player[i] = input(f"Choose a colour (blue, green, orange, pink, red or yellow) for position number {i + 1}: ")
        while player[i] not in colours:
            print(
                "Wrong entry. Please enter a colour (no space, all small letters) from blue, green, orange, pink, red and yellow")
            player[i] = input(
                f"Choose a colour (blue, green, orange, pink, red or yellow) for position number {i + 1}: ")
