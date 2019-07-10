def bet():
    """ returns how much the player wants to bet on each round of the game"""

    game_bet = (input("If you want to play, you have to bet.\n How much do you want to bet this round?"))
    if game_bet.isnumeric() == True:
        game_bet = int(game_bet)
    else:
        print("Please input a number.")
        sys.exit()
    return (game_bet)
