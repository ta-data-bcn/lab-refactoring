
# pad printing function (uses global variable: defaultPad)
# takes as input the choices of marked spaces by cpu and player
# assigns an 'O' and 'X' marks for the player and cpu choices
# the Tic Tac Toe pad is printed one row at a time from a list of lists

def printPad(cpuHistory,playerHistory,pad=defaultPad):
    nRows = len(pad)
    
    # check for the player options
    if playerHistory:
        for i in range(len(playerHistory)):
            pad[playerHistory[i][0]][playerHistory[i][1]] = 'O '
            
    # check for CPU options
    if cpuHistory:
        for i in range(len(cpuHistory)):
            pad[cpuHistory[i][0]][cpuHistory[i][1]] = 'X '
    
    # print Pad!
    for i in range(3):
        print(pad[i])