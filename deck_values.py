
def hand_sum(hand, a_as_one):
    """
    Calculate the sum of a hand given a hand (list) and the values (dictionary) and a boolean to chose the value of ACE

    :param hand: (list) list of cards we want to calculate the value of
    :param a_as_one: (bool) defines if the ace should count as 11 (=True) or 1 (=False)
    :return: (int) total sum of the value of the given hand
    """
    values = {}
    hearts = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for card in hearts:
        if card in ['J', 'Q', 'K']:
            values[card] = 10
        elif card == 'A' and a_as_one is True:
            values[card] = 1
        elif card == 'A' and a_as_one is False:
            values[card] = 11
        else:
            values[card] = int(card)
    total = 0

    for card in hand:
        total += values[card]
    return total