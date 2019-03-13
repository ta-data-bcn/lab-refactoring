"""
# This library has useful methods related to cards: give cards to player/dealer, sum card values...

"""

import random

# We define the deck the players will use
# Face cards are J, Q, K, A
face_cards = {'A': [11, 1], 'K': 10, 'Q': 10, 'J': 10}
deck = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]


# First we ask the user to place the bet.
def place_bet():
    user_input = input('Please, introduce your bet: ')

    # Check if he has introduced a correct value
    if user_input.isdigit():
        return int(user_input)
    else:
        print('You introduced a non valid character. Please introduce a number')


# Deal the first two cards.
def deal_first_hand():
    return [random.choice(deck) for i in range(2)]


# Deal an additional card.
def deal_card():
    return random.choice(deck)


def parse_ace_value(hand, value):
    """
    # Choose value of Ace, we'll use it when asking the player which value does he want for the Ace.
    # There's no return because we will use it in combination with other functions that return the hand.

    :param hand: list
    :param value: int
    :return: No return
    """
    for i in range(len(hand)):
        if hand[i] == 'A':
            hand[i] = value


# Check natural blackjack, we parse Ace to 11 automatically.
def natural_blackjack(hand):
    """
    # Check if the player has 21 points with the first 2 cards.
    # In this case, the Ace gets converted to 11 automatically.

    :param hand: list
    :return: sum of cards in hand
    """
    if check_score(hand) == 21:
        parse_ace_value(hand, 11)
        parse_face_cards(hand)
    return sum(hand[:2]) == 21


# Check if player has two cards of the same denomination.
def check_denomination(hand):
    return hand[0] == hand[1]


def check_double_down(hand):
    """
    # Check if the first 2 cards sum 9, 10 or 11

    :param hand: list
    :return: sum of cards in hand
    """
    result = sum(hand[:2])
    return result == 9 or result == 10 or result == 11


def check_score(hand):
    """
    # If user has an Ace, ask him which value does he want to give to it.
    # After that, convert the face cards to their numerical value.
    # Finally, sum the total value of the hand and return the result.

    :param hand: list
    :return: total value of cards in hand
    """
    if 'A' in hand:
        p_input = int(input("Would you like your ace to be a 1 or an 11? "))
        parse_ace_value(hand, p_input)
    parse_face_cards(hand)
    return sum(hand)


def compare_hands(p_hand, d_hand, bet):
    """
    # Use check_score() to calculate the value of both hands.
    # Apply conditions to check the outcome of the game and print it on the screen of the player.

    :param p_hand: list
    :param d_hand: list
    :param bet: int
    :return: No return
    """
    p_score = check_score(p_hand)
    d_score = check_score(d_hand)

    if p_score > 21:
        print("You bust with %d points. Dealer wins" % p_score)

    elif d_score > 21:
        print("Dealer busts with %d points. Players wins" % d_score)

    elif p_score == d_score:
        print("There has been a tie. Player points: %d and hand: %s. Dealer points: %d and hand: %s" % (
            p_score, p_hand, d_score, d_hand))

    elif p_score > d_score:
        print("Player wins with %d points with the hand %s, you win %d€" % (p_score, p_hand, bet))

    elif p_score < d_score:
        print("Dealer wins with %d points with the hand %s" % (d_score, d_hand))


def hit(hand):
    """
    # Check the score of the player, to see if he actually can ask for a new card.
    # If he can, add a new card to the player_hand list (to his hand)

    :param hand: list
    :return: No return
    """
    new_card = deal_card()

    if check_score(hand) < 21:
        hand.append(new_card)

    else:
        print("You cannot ask for more cards")


def parse_face_cards(hand):
    """
    # We change the letters of the face cards, to their numerical value.
    # No return, since function we'll be used in combination with other functions that do return the hand.

    :param hand: list
    :return: No return
    """
    for i in range(len(hand)):
        if hand[i] == 'K':
            hand[i] = face_cards['K']

        if hand[i] == 'Q':
            hand[i] = face_cards['Q']

        if hand[i] == 'J':
            hand[i] = face_cards['J']


def dealer_play(hand):
    """
    # Dealer will only play as long as he has 14 points or less.
    # While condition applies (<=14), add cards to dealer's hand.

    :param hand: list
    :return: list
    """
    while check_score(hand) <= 14:
        hit(hand)
    print("Dealer's hand: ", hand)
    return hand
