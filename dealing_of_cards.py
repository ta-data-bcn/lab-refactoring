import random
import sys
deck_cards = [2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"] *4

"""function for dealing of cards"""

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
