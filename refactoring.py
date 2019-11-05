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

###
### hacer list comprehension diccionario
###

for hole in board:
    col = random.choice(colors)
    codemaker[hole] = col

pos_choices = {}

# Let player choose the color pegs for each position. Constraint him/her to choose only accepted colors (string it to lowercase).

rounds = 0

has_won = False

def user_choice (pos):
    choice = input(f"Choose your color for position {pos}: ")
    while choice.lower() not in colors:
        choice = input("Remember choosing your colors within 'red', 'blue', 'yellow', 'green' or 'orange': ")
    pos_choices[pos] = choice

def check_res (key, value):
    if value == codemaker[key]:
        results.append('black')
    elif value in codemaker.values():
        results.append("grey")
    else:
        results.append("white")

while rounds < 5 and has_won == False:

    for pos in ['A', 'B', 'C']:
        user_choice(pos)
    
    results = []

    for key, value in pos_choices.items():
        check_res(key, value)

    print("Your results are: position A:", results[0], ", position B:", results[1], "and position C:", results[2])

    rounds += 1
    
    if all([result == 'black' for result in results]):
        has_won = True

if has_won:
    print('You have won!')
else:
    print('Codemaker was too much for you!')