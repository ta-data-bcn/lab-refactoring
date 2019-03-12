import deck_values as dv
import player_action as pa
import time


def settle_player(player_sum, player_hand, player_ace_as_one):
    """
    Enables the play of the player and updates the player status: if busted, the sum of the hand and the action to take
    :param player_sum: (int) current sum of the hand
    :param player_hand: (list) hand of the player
    :param player_ace_as_one: (bool) defines whether the ace need to be counted as 1 (=True), False otherwise
    :return: returns a tuple with 3 elements (bool, int, str) that define the status of the player
    busted (=True) or not, sum of the hand and action required from the player
    """
    player_busted = False

    if player_sum > 21 and 'A' not in player_hand:
        print(player_hand, "\nYou are now at", player_sum, "\nBusted!")
        action = "pass"
        player_busted = True

    elif player_sum > 21 and 'A' in player_hand:
        player_ace_as_one = True
        player_sum = dv.hand_sum(player_hand, player_ace_as_one)

        if player_sum > 21:
            print(player_hand, "\nYou are now at", player_sum, "\nBusted!")
            action = "pass"
            player_busted = True
        else:
            action = pa.decide_player_action(player_hand, player_sum)

    elif player_ace_as_one:
        action = pa.decide_player_action(player_hand, player_sum)

    else:
        action = pa.decide_player_action(player_hand, player_sum)

    return player_busted, player_sum, action


def settle_dealer(dealer_sum, dealer_hand):
    """
    Makes the dealer play and updates its status
    :param dealer_sum: (int) total sum of the dealer's initial hand
    :param dealer_hand: (list) dealer's initial hand
    :return: Tuple with 2 elements (bool, int) that define the status of the dealer
    busted (=True) or not and sum of the hand
    """
    if dealer_sum > 21 and 'A' not in dealer_hand:
        print("The dealer's hand is:", dealer_hand, "\nDealer is busted")
        dealer_busted = True

    elif dealer_sum > 21 and 'A' in dealer_hand:
        dealer_ace_as_one = True
        dealer_sum = dv.hand_sum(dealer_hand, dealer_ace_as_one)

        if dealer_sum > 21:
            print("The dealer's hand is:", dealer_hand, "\nDealer is busted!")
            dealer_busted = True
    else:
        print("The dealer's hand is:", dealer_hand, "\nWith a total score of", dealer_sum)
    return dealer_busted, dealer_sum



def settle_game(player_status, player_hand, dealer_status, dealer_hand, pot, bet):
    """
    Settles the whole round and updates the pot of the player
    :param player_status: (tupl) tuple with 3 elements (bool, int, str) that define the status of the player
    busted (=True) or not, sum of the hand and action required from the player
    :param player_hand: (list) list containing strings that represent the cards of the player's hand
    :param dealer_status: (tupl) Tuple with 2 elements (bool, int) that define the status of the dealer
    busted (=True) or not and sum of the hand
    :param dealer_hand: (list) list containing strings that represent the cards of the player's hand
    :param pot: (int) total pot of the player
    :param bet: (int) bet of the current round
    :return: (int) the updated pot
    """
    time.sleep(1)
    if player_status[0]:
        pot = pot - bet
        print(f"The dealer wins\n Your remaining pot is ${pot}")
    elif dealer_status[0]:
        pot = pot + bet
        print(f"You win!\n You have now ${pot} in your pot")
    else:
        if dealer_status[1] == 21 and player_status[1] == 21:
            if 'A' in dealer_hand not in player_hand:
                pot = pot - bet
                print(f"The dealer wins\n Your remaining pot is ${pot}")
            elif 'A' in player_hand not in dealer_hand:
                pot = pot + bet
                print(f"You win!\n You have now ${pot} in your pot")
            else:
                print("It's a split")
        else:
            if dealer_status[1] > player_status[1]:
                pot = pot - bet
                print(f"The dealer wins\n Your remaining pot is ${pot}")
            elif dealer_status[1] < player_status[1]:
                pot = pot + bet
                print(f"You win!\n You have now ${pot} in your pot")
            else:
                print(f"It's a split\n You have now ${pot} in your pot")
    return pot
