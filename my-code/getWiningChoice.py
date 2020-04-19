
# import negative function
from numpy import negative
from determine_direction import determine_direction

# this function takes a potential wining pair of points as input (in two tuples)
# it returns the corresponding point that makes a wining line in Tic Tac Toe (in a tuple)
# uses global variable: ticTacDict

def getWiningChoice(tuples2win,gameDict):
    (cosTheta,sinTheta) = determine_direction(*tuples2win)
    
    for aTuple in gameDict.values():
        if (aTuple != tuples2win[0]) & (aTuple != tuples2win[1]):
            (cosGamma,sinGamma) = determine_direction(tuples2win[1],aTuple)
            
            if ((cosTheta,sinTheta) == (cosGamma,sinGamma)) | \
            ((cosTheta,sinTheta) == negative((cosGamma,sinGamma))).all():
                return aTuple