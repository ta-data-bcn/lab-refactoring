import deck_values as dv
import player_action as pa
import time


def settle_player(player_status, player_ace_as_one):
    """
    Enables the play of the player and updates the player status: if busted, the sum of the hand and the action to take
    :param player_status: (list) current status of the player
    :param player_ace_as_one: (bool) defines whether the ace need to be counted as 1 (=True), False otherwise
    :return: returns a tuple with 3 elements (bool, int, str) that define the status of the player
    busted (=True) or not, sum of the hand and action required from the player
    """

    if player_status[1] > 21 and 'A' not in player_status[2]:
        print(player_status[2], "\nYou are now at", player_status[1], "\nBusted!")
        player_status[3] = "pass"
        player_status[0] = True

    elif player_status[1] > 21 and 'A' in player_status[2]:
        player_ace_as_one = True
        player_status[2] = dv.hand_sum(player_status[2], player_ace_as_one)

        if player_status[1] > 21:
            print(player_status[2], "\nYou are now at", player_status[1], "\nBusted!")
            player_status[3] = "pass"
            player_status[0] = True
        else:
            player_status[3] = pa.decide_player_action(player_status[2], player_status[1])

    elif player_ace_as_one:
        player_status[3] = pa.decide_player_action(player_status[2], player_status[1])

    else:
        player_status[3] = pa.decide_player_action(player_status[2], player_status[1])

    return player_status


def settle_dealer(dealer_status):
    """
    Makes the dealer play and updates its status
    :param dealer_status: (list) current status of the dealer
    :return: Tuple with 2 elements (bool, int) that define the status of the dealer
    busted (=True) or not and sum of the hand
    """
    if dealer_status[1] > 21 and 'A' not in dealer_status[2]:
        print("The dealer's hand is:", dealer_status[2], "\nDealer is busted")
        dealer_status[0] = True

    elif dealer_status[1] > 21 and 'A' in dealer_status[2]:
        dealer_ace_as_one = True
        dealer_status[1] = dv.hand_sum(dealer_status[2], dealer_ace_as_one)

        if dealer_status[1] > 21:
            print("The dealer's hand is:", dealer_status[2], "\nDealer is busted!")
            dealer_status[0] = True
    else:
        print("The dealer's hand is:", dealer_status[2], "\nWith a total score of", dealer_status[1])
    return dealer_status


def settle_game(player_status, dealer_status, pot, bet):
    """
    Settles the whole round and updates the pot of the player
    :param player_status: (list) List with 4 elements (bool, int, list, str) that define the status of the player
    busted (=True) or not, sum of the hand, hand of the player and action required from the player and
    :param dealer_status: (list) List with 3 elements (bool, int, list) that define the status of the dealer
    busted (=True) or not, sum of the hand and the hand of the dealer
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
            if 'A' in dealer_status[2] not in player_status[2]:
                pot = pot - bet
                print(f"The dealer wins\n Your remaining pot is ${pot}")
            elif 'A' in player_status[2] not in dealer_status[2]:
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
