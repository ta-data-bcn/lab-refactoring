
# input player function (uses global variable: ticTacDict)
# takes as input the choices of marked spaces by cpu and player
# Error handling is very important on selecting a proper Tic Tac Toe:
# 1) string typos are checked (case insensitive and strip spaces)
# 2) must be a choice that hasn't been selected yet (cpu or player history)

def input_player_choice(cpuHistory,playerHistory,gameDict=ticTacDict):
    
    print('This is the game now:')
    printPad(cpuHistory,playerHistory)
    yourChoice = input("Choose your mark! (e.g: 'L' stands for 'Left') ")

    while True:
        # check if input is among dictionary keys
        if yourChoice.upper().strip(" ") in gameDict.keys():
            # check if input has already been selected
            if gameDict[yourChoice.upper().strip(" ")] in (playerHistory + cpuHistory):
                yourChoice = input("Choose another one! It has been already chosen! ")
            else:
                return gameDict[yourChoice.upper().strip(" ")]
        else:
            yourChoice = input("Select a proper position! ")