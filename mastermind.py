# Create colors to choose
# Create positions where to put the pegs 
# Randomly assign the combination of pegs
# Let player choose the color pegs for each position. Constraint him/her to choose only accepted colors (string it to lowercase).
# Return error message if they don't choose 3 or not accepted strings.
# Return the hints or victory or defeat. Create a loop with the maximum number of tries.

import random

# Create colors to choose

colors = ['red', 'blue', 'yellow', 'green', 'orange']

# Create positions where to put the pegs 

board = ['A', 'B', 'C']

# Randomly assign the combination of pegs
#[x == 1 for x in range(3)]
codemaker = {}

for hole in board:
    col = random.choice(colors)
    codemaker[hole] = col

#print(codemaker)

#Create dictionary for choices

pos_choices = {}

# Let player choose the color pegs for each position. Constraint him/her to choose only accepted colors (string it to lowercase).

rounds = 0

while rounds < 5:
    if rounds == 4:
        print("I'm sorry, codemaker was too much for you.")
        break
    else:
        rounds += 1

    A_choice = input("Choose your color for position A: ")

    while A_choice.lower() not in colors:
        A_choice = input("Remember choosing your colors within 'red', 'blue', 'yellow', 'green' or 'orange': ")
    pos_choices['A'] = A_choice

    B_choice = input("Choose your color for position B: ")
    while B_choice.lower() not in colors:
        print("Remember choosing your colors within 'red', 'blue', 'yellow', 'green' or 'orange': ")
        B_choice = input()
    pos_choices['B'] = B_choice

    C_choice = input("Choose your color for position C: ")
    while C_choice.lower() not in colors:
        print("Remember choosing your colors within 'red', 'blue', 'yellow', 'green' or 'orange': ")
        C_choice = input()
    pos_choices['C'] = C_choice

    # Associate values to pos_choices

    results = []

    for key, value in pos_choices.items():
        if value == codemaker[key]:
            results.append('black')
        elif value in codemaker.values():
            results.append("grey")
        else:
            results.append("white")

    print("Your results are: position A:", results[0], ", position B:", results[1], "and position C:", results[2])

    if not all([result == 'black' for result in results]) and rounds <4:
        print('Try it again!')
    elif not all([result == 'black' for result in results]):
        continue
    else: 
        print('You have won!')
        break


# Assign colors

