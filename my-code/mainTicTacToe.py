"""
This is the refactored version of my first project (Tic Tac Toe game)

The code is refactored from Jupyter Notebook to this python main file.
Functions are imported from different Python scripts.
"""

# import functions from scripts
from printPad import printPad
from input_first_choice import input_first_choice
from input_player_choice import input_player_choice
from gen_random_move import gen_random_move
from predict_wining import predict_wining
from getWiningChoice import getWiningChoice
from determine_winner import determine_winner

# main code: TicTacToe!
if __name__ == '__main__':

    # INITIALIZATION OF VARIABLES
    
    # Tic Tac Toe Pad
    defaultPad = [['Lt','t ','Rt'],['L ','m ','R '],['Lb','b ','Rb']]

    # Tic Tac Toe dictionary, keys from Pad, values are indexes (or coordinates)
    ticTacDict = {'LT':(0,0), 'T':(0,1), 'RT':(0,2),\
                  'L':(1,0), 'M':(1,1), 'R':(1,2),\
                  'LB':(2,0), 'B':(2,1), 'RB':(2,2)}

    # number of marks in Pad (initial zero)
    markedSpaces = 0

    # Who will begin?
    firstChoice = input_first_choice()

    # Initialize cpu history of choices
    if firstChoice == 'cpu':
        # First cpu choice default --> center of the pad
        cpu_choices = [(1,1)]
        markedSpaces += 1
    else:
        # Initialize empty
        cpu_choices = []

    # Initialize the player history of choices
    player_choices = []
    
    # While loop is broken inside
    while True:

        playerChoice = input_player_choice(cpu_choices,player_choices,ticTacDict,defaultPad)
        player_choices.append(playerChoice)
        markedSpaces += 1
        # check player winner to break
        playerWins = determine_winner(player_choices,ticTacDict)
        if playerWins:
            break
        elif markedSpaces == 9:
            # all marked Spaces --> break
            break

        # cpu looking for its wining chance
        tuples2win = predict_wining(cpu_choices)
        if tuples2win:
            # pick always the last pair of tuples
            cpu_choice = getWiningChoice(tuples2win[-1],ticTacDict)
        else:
            # cpu just does a random move
            cpu_choice = gen_random_move(cpu_choices,player_choices)

        if (not cpu_choices) & ((1,1) not in player_choices):
            # Cpu first choice always check the center
            cpu_choice = (1,1)
        elif cpu_choice in player_choices:
            # Over-write cpu_choice in case is already chosen by player
            cpu_choice = gen_random_move(cpu_choices,player_choices)

        cpu_choices.append(cpu_choice)
        markedSpaces += 1
        # check cpu winner to break
        cpuWins = determine_winner(cpu_choices,ticTacDict)
        if cpuWins:
            break
        elif markedSpaces == 9:
            # all marked Spaces --> break
            break
            
    # Game conclusion (cpuWins, playerWins or Tied)
    if cpuWins:
        print("You have been beaten :(")
        printPad(cpu_choices,player_choices,defaultPad)
    elif playerWins:
        print("You are the champion, my friend :)")
        printPad(cpu_choices,player_choices,defaultPad)
    else:
        print("Tic Tac Toe Tied!!! Play again :)")
        printPad(cpu_choices,player_choices,defaultPad)
