
# import randint function
from random import randint

# get a random choice for a cpu Tic Tac Toe move
# takes as input the choices of marked spaces by cpu and player
# Error handling is very important:
# Random choice must not be selected before (either by cpu or player)

def gen_random_move(cpuHistory,playerHistory):
    while True:
        pos0 = randint(0,2)
        pos1 = randint(0,2)
        if len(playerHistory+cpuHistory) == 9:
            # break to avoid infinite loop in case I get here
            break
        elif (pos0,pos1) not in (playerHistory + cpuHistory):
            return (pos0,pos1)