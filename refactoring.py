#BlackJack
import random
import sys
import game_function as gf  # saved function
from bet_function import bet # saved function

# divide all funcitons into different .py files, call accordingly as needed
# following variables are needed throught all code:
deck_cards = [2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"] *4

#start of game message

print ("This is Blackjack, welcome!")
play = input ("Start Game? [Y/N]")

# error handeling
if play != "Y" and play != "N":
        print ("Make sure your answer is in CAPITAL LETTERS")
        play = input("Do you want to play again [Y/N]? ")
elif play != "Y" and play != "N":
        print ("Wrong input again. Restart the game")
        sys.exit()

player_value = input("How much money do you want to change into chips [intiger, no currency]? ")

# error handeling
if player_value.isnumeric():
    player_value = int(player_value)
else:
    print ("Make sure to enter a numberic value. You will have to re-start the game.")
    sys.exit()

# game loop
# actual game while loop, includes an again function and a function for being out of money
value = player_value # amount of money player has left
again = 0 # count variable to start game

while again == "Y" or play == "Y" and value >0:
    game_bet = bet()
    print ("Your current value is of %s, you bet %s"% (value, game_bet))
    game_win = gf.game()
    if game_win >=1:
        value += game_bet
        print ("Your current value is of %s"% (value))
    else:
        value -= game_bet
        print ("Your current value is of %s"% (value))
    again = input("Do you want to play again [Y/N]? ")
    if again != "Y" and again != "N":
            print ("Make sure your answe is in CAPITAL LETTERS")
            again = input("Do you want to play again [Y/N]? ")
    elif again != "Y" and again != "N":
            print ("Wrong input")
            sys.exit()
    if again == "N":
        play = "N"
        print ("End of Game")

