def deck_values(a_as_one):
    """
    Define the values for each card of the deck depending on the desired value for the ace cards.
    :param a_as_one: boolean, =True if we want the ace to count as one, =False if we want the ace to count 11
    :return: Dictionary with keys = cards (strings) and values = values of each card (int)
    """
    values_of_the_deck = {}
    hearts = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for card in hearts:
        if card in ['J', 'Q', 'K']:
            values_of_the_deck[card] = 10
        elif card == 'A' and a_as_one is True:
            values_of_the_deck[card] = 1
        elif card == 'A' and a_as_one is False:
            values_of_the_deck[card] = 11
        else:
            values_of_the_deck[card] = int(card)
    return values_of_the_deck


def hand_sum(hand, values):
    """
    Calculate the sum of a hand given a hand (list) and the values (dictionary)

    :param hand: (list) list of cards we want to calculate the value of
    :param values: (dict) value sof each card
    :return: (int) total sum of the value of the given hand
    """
    total = 0
    for card in hand:
        total += values[card]
    return total