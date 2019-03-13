import functions

# List of global variables for the game
tries = 10
number_colors = 4
options = ['blue', 'green', 'red', 'yellow', 'white', 'black']

# Step 1 of the game: the machine picks the color-code.
machine_code = functions.machine_picks_colors(options, number_colors)

# Step 2 of the game: player picks the color-code and plays.
for i in range(tries):

    person_guess = functions.player_picks_colors(options, number_colors)

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
