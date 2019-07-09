# Mastermind game player vs computer

# Import libraries to be used in the code below
import random
# Define a function to ask the player to choose 4 colours between blue, green, orange, pink, red, yellow
import ask_player
## Define a random generator function to generate the computer choice of colours and positions
import random_colour
## Define a function to give the result of a round:
### Black means the right colour in the right position
### White means this colour is present in the computer choice but in the wrong position
import give_result


# Set the variables respectively for the choice of the computer, the choice of the player, the number of rounds
# and define the colours available.
computer = []
player = ["", "", "", ""]
round_number = 10
colours = ["blue", "green", "orange", "pink", "red", "yellow"]


# Define the choice colours of the computer

## The result of randomColour is a list that I transform to a tuple called computer_tuple so it stays unchanged as a
## reference for the initial computer choice of colours.
## NOTE: The computer variable is modified during the giveResult function (for reasons I don't have time to solve
## now). That is why I need to create and use computer_tuple.
computer_tuple = tuple(random_colour())


# Define the choice of the computer
computer = random_colour()

# Play the game. The game is composed of a maximum of 10 rounds. if after 10 rounds the user has not found the
# computer's choice then the computer wins
for i in range(10):
    print(f"This is round number {i + 1}")
    ask_player()
    result2 = give_result()
    if result2 == ["black", "black", "black", "black"]:
        print("Congratulations! You won!!")

if result2 != ["black", "black", "black", "black"]:
    print(f"Sorry but you lost. The answer was {computer_tuple}")