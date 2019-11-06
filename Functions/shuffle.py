''' This is the function for shuffeling the card of the deck and pop those cards from the deck because 
they can not be repeated.'''
import re
import random 


def shuffle_card(deck):
    hand = []
    for x in range(2):
        card = deck.pop()
        hand.append(card)
    return hand 


#print(shuffle_card)