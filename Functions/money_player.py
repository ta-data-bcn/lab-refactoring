''' In this function, the player input the quantity we wants to play during the whole game.'''


import re 
def money_player(money):
    
    exit = True
    while exit==True:
        money = input("\n How much money do you want to play in the game? The minimum is 60 and maximum is 150.  ")
        if re.match("^([6-8][0-9]|9[0-9]|1[0-4][0-9]|150)$",money) is not None:
            return int(money)
            exit == False
            
        else:
            print("\n Sorry, you quantity is not accepted for playing. The dealer kick you out from the table.")
            return 'error'
            
            exit = False

