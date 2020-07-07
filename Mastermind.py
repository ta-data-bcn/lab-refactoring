#!/usr/bin/env python
# coding: utf-8

# # Mastermind

# Import libraries
import random

# **Create colors available:**
colors=["blue", "red", "green", "purple", "yellow", "black", "orange", "grey"]

# **Choose number of rounds**
max_rounds = int(input('Choose max number of rounds: '))

# **Define round variable**
n_round = 0

# **Generate random hidden combination**
hide = random.choices(colors,k=4)

# **Player choose colors**
def player():
    player_combination = []

    while len(player_combination)<4:
        def player_input():
            a=input('Choose a color in the list: ')
                         
            try:
                player_combination.append(colors[colors.index(a)])
                
            except:
                print('color chosen is not in list')
                player_input()
            
        player_input()

    print('your combination is ', player_combination)
    return player_combination

# **Challenger answer**
def challenger(player,hide):
    challenger_advise = []

    for i,j in zip(player,hide):
        if i==j:
            challenger_advise.append('red')
        elif i in hide:
            challenger_advise.append('white')
        else:
            challenger_advise.append(" ")
    
    if challenger_advise.count('red')>2 and 'white' in challenger_advise:
        challenger_advise.insert(challenger_advise.index('white')," ")
        challenger_advise.remove('white')
            
    print(challenger_advise)
    return challenger_advise

# **Round execution**
def round_result(challenger):
    result = 0
    if challenger==['red','red','red','red']:
        result = 1
        print('Congratulations, you won !')
    else:
        result = 0
        
    return result

# ### Game execution

# **List of colors:**
# <font color = blue>blue</font>, <font color = red>red</font>, <font color = green>green</font>,
# <font color = purple>purple</font>, <font color = yellow>yellow</font>, <font color = black>black</font>, <font color = orange>orange</font>, <font color = grey>grey</font>

player_won = 0

print('Choose between the following colors: ', colors)

while player_won == 0 and n_round<max_rounds:
    player_won = round_result(challenger(player(),hide))
    n_round +=1
    
if n_round == max_rounds and player_won == 0:
    print('Sorry, you lose')
    print('The hidden combination was', hide)
