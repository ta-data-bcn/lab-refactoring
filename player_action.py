import time

def decide_player_action(player_hand, player_hand_value):
    """
    Defines the action of the player for a given hand and value
    :param player_hand: list of the cards of the player
    :param player_hand_value: value related to the hand of the player
    :return: (str) 'hit' or 'pass'
    """
    time.sleep(1)
    options = ["hit", "pass"]
    player_choice = ""
    print("Your hand is", player_hand, "You are now at", player_hand_value)

    while player_choice not in options:
        player_choice = str(input(f"You can {options}, what would you like to do?\n"))
    return player_choice


def decide_keep_playing(pot):
    """
    Defines if the game is over due to empty pot or, if not, gives the player the choice to continue.
    :param pot: (int) remaining pot
    :return: (bool) True if a new round will be player, False exits the game
    """
    if pot >= 5:
        keep = input("Do you want to keep playing Y/N ")

        while keep not in ['Y', 'N']:
            keep = input("Do you want to keep playing Y/N ")

        return keep == 'Y'
    else:

        print("You don't have enough chips on your pot :(")
        return False
