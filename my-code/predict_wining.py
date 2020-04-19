
# function predicting possible player/cpu win !
# it could be used in two possibilities:
# a) enter cpu history to predict my next wining move
# b) enter player history to predict a possible wining move
# it returns the predicted wining pair (or pairs) of marks as a tuple

def predict_wining(movesHistory):
    tuples2win = []
    nMoves = len(movesHistory)
    for i in range(nMoves):
        for j in range(nMoves):
            if j > i:
                # check horizontal or vertical
                if (movesHistory[i][0] == movesHistory[j][0]) | \
                (movesHistory[i][1] == movesHistory[j][1]):
                    tuples2win.append((movesHistory[i],movesHistory[j]))
                # check one Tic Tac Toe possible diagonal
                elif (movesHistory[i][0] == movesHistory[i][1]) & \
                (movesHistory[j][0] == movesHistory[j][1]):
                    tuples2win.append((movesHistory[i],movesHistory[j]))
                # check the other Tic Tac Toe possible diagonal
                elif (sum(movesHistory[i]) == 2) & (sum(movesHistory[j]) == 2):
                    tuples2win.append((movesHistory[i],movesHistory[j]))
    return tuples2win