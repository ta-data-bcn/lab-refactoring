"""BlackJack"""
""""for the hand"""
# Card deck:
# Define the deck and the values in the deck
# Change planned dictionary to list - dictionary will not work as once a card is layed down, the card has to be removed from the stack
import random
import sys

deck_cards = [2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"] *4

def deal_cards():
    hand = []
    for i in range (2):
        card = deck_cards[random.randint (0,12)]
        hand.append (card)
    return hand

"""deck for hit"""
# if player chooses to hit following happens:
def hit(hand):
    hand2 = hand
    card = deck_cards[random.randint (0,12)]
    hand2.append(card)
    return hand2

"""For player's hand"""
# Player game, what is the sum of the player's hand
# assumption that player will play an intiger and not a letter
        # >> for error handling code - see
# include special funciton for A (1 or 11)
def player (hand):
    player_points = 0
    player_hand = []
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            player_hand.append(10)
        elif card == "A":
            A = int(input("Do you want to play 1 or 11 [1, 11]?"))
            player_hand.append(A)
        else:
            player_hand.append(card)
    player_hand = sum(player_hand)
    player_points += player_hand
    return player_points

"""For the dealers hand"""
# Dealer game what is the sum of the dealer's hand
# include special funciton for A (1 or 11 depending on the total score

def dealer(hand):
    dealer_points = 0
    dealer_hand = []
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            dealer_hand.append(10)
        elif card == "A":
            if len(dealer_hand) > 2 and (dealer_hand[0]+dealer_hand[1])> 11:
                dealer_hand.append(1)
            else:
                dealer_hand.append(11)
        else:
            dealer_hand.append(card)
    dealer_hand = sum(dealer_hand)
    dealer_points += dealer_hand
    return dealer_points

"""Game function"""
def game():

    wins = 0

    player_hand = deal_cards()
    dealer_hand = deal_cards()

    print (f"You have {player_hand}")
    print (f"The dealer has {dealer_hand}")

    ppoints = player(player_hand)
    dpoints = dealer(dealer_hand)

    print (f"You have a total of {ppoints}")
    print (f"The dealer has a total of {dpoints}")

# blackjack exception
    blackjack = False
    if ppoints == 21:
        print ("You win with blackjack!")
        wins += 1
        blackjack = True
    if ppoints > 21:
        print ("You lose, over 21")
        blackjack = True

    if dpoints == 21:
        print ("You lose, dealer has blackjack!")
        blackjack = True
    if dpoints > 21:
        print ("You win, dealer over 21")
        wins +=1
        blackjack = True

# choice to hit or stand
    if not blackjack:
        choice = input("Do you want to hit or stand [h/s]?")
        if choice != "h" and choice != "s":
            print ("Wrong input, make sure you enter only h or s [h/s], you have one more chance or the game will end automatically.")
            choice = input("Do you want to hit or stand [h/s]?")
            if choice != "h" and choice != "s":
                print ("Wrong input. ")
                sys.exit()
        elif choice == "h":
            player_hand = hit(player_hand)
            print (f"You now have {player_hand}")
            ppoints = player (player_hand)
            print (f"you have a total of {ppoints}")
        if dpoints < 17:
            dealer_hand = hit(dealer_hand)
            print (f"The dealer now has {dealer_hand}")
            dpoints = dealer(dealer_hand)
            print (f"for a total of {dpoints}")
        else:
            print (f"The dealer still has {dealer_hand}, for a total of {dpoints}")

# score reslution
        if ppoints == 21:
            print ("You win!")
            wins += 1
        elif dpoints == 21:
            print ("You lose!")
        elif ppoints > 21:
            print ("You lose!")
        elif dpoints > 21:
            print ("You win!")
            wins += 1
        elif ppoints < dpoints:
            print ("You lose!")
        elif ppoints > dpoints:
            print ("You win!")
            wins += 1
        else:
            print ("You lose!")

    return wins

"""run game"""

import random
import sys


# start of game message
print ("This is Blackjack, welcome!")

play = input ("Start Game? [Y/N]")
# making variables fail proof
if play != "Y" and play != "N":
        print ("Make sure your answe is in CAPITAL LETTERS")
        play = input("Do you want to play again [Y/N]? ")
elif play != "Y" and play != "N":
        print ("Wrong input again. Restart the game")
        sys.exit()

player_value = input("How much money do you want to change into chips [intiger, no currency]? ")
# making variables fail proof
if player_value.isnumeric():
    player_value = int(player_value)
else:
    print ("Make sure to enter a numberic value. You will have to re-start the game.")
    sys.exit()

# defining the bet value

def bet():
    game_bet = (input("If you want to play, you have to bet.\n How much do you want to bet this round?"))
    if game_bet.isnumeric() == True:
        game_bet = int(game_bet)
    else:
        print ("Please input a number.")
        sys.exit ()
    return (game_bet)

value = player_value
again = 0

# actual game while loop, includes an again function and a function for being out of money

while again == "Y" or play == "Y" and value >0:
    game_bet = bet()
    print ("Your current value is of %s, you bet %s"% (value, game_bet))
    game_win = game()
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
