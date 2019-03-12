from random import choice
import time


def deal_cards(deck):
    """
    Randomly chooses two cards of the deck for the player and for the dealer.
    :param deck:
    :return: The hand of the player and the dealer. List of lists of 2 elements (str)
    """
    dealing = ["Dealing...","...","...","..."]
    for line in dealing:
        print(line,)
        time.sleep(0.2)

    player_hand = [choice(deck) for x in range(2)]
    dealer_hand = [choice(deck) for x in range(2)]

    return player_hand, dealer_hand

def deal_one(hand, deck):
    return hand.append(choice(deck))
