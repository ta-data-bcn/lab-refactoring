# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# The original game was one big chunk of code, following discussions and impact studies 
# with my good teammate Anna R., we agreed upon the following changes :
# - creating a separated 'game_functions' file which centralises all used functions
# - the game itself is now just a few lines of codes, and import all the needed functions for the other Python file

# ToDo for possible new versions : use a dictionary (key : colour, value : integer) instead of a list of selected coloured balls
# Code the game using a Dictionary to compare the dictionary's value instead of the text

from game_functions import *

rounds_10 = 11
round_number = 0

print("Welcome to the great MasterMind game ! \nHave you what it takes to break the code ? \nYou have 10 turns to prove your value, my very young Padawan")

computer_Mastercode = random_cpu()

#print(computer_Mastercode)

#Overall finale results
round_number = 1

while round_number<rounds_10 :
    print("\n welcome to round #",round_number,"\n")
    player_guess = player_select()
    each_round_check(computer_Mastercode,player_guess)
    round_number +=1
    if computer_Mastercode == player_guess:
        break    
    
finale_result(player_guess,computer_Mastercode)


# %%


