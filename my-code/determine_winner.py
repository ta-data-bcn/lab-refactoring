
# import negative function
from numpy import negative
from determine_direction import determine_direction

# this function verifies if there's a winner (three points in a line)
# uses global variable: ticTacDict

def determine_winner(movesHistory,gameDict):
    nMoves = len(movesHistory)
    if nMoves >= 3:
        for i in range(nMoves):
            for j in range(nMoves):
                if j > i:
                    (cosTheta,sinTheta) = determine_direction(movesHistory[j],movesHistory[i])
                for k in range(nMoves):
                    if (j > i) & (k > j):
                        (cosGamma,sinGamma) = determine_direction(movesHistory[k],movesHistory[j])
                        if ((cosTheta,sinTheta) == (cosGamma,sinGamma)) | \
                        ((cosTheta,sinTheta) == negative((cosGamma,sinGamma))).all():
                            return True
    return False