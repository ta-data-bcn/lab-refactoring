import re
import sys


def place_bet(pot):
    """
    The player places the bet at the beginning of each round
    :param pot: total amount of money remaining for the player (int)
    :return: bet (int)
    """
    bet = 0
    while (bet < 5) or (bet > 200):
        bet = input(
            "How much money do you want to bet on this round?. The maximum bet is $200 and the minimum bet is $5\n")
        if re.findall(r"(?<!\.)\b[0-9]+\b(?!\.)", bet):
            bet = int(bet)
            if bet > pot:
                print(f"You don't have that much, your current pot is ${pot}")
                bet = 0
            else:
                if bet < 5:
                    print("The minimum bet is $5")
                elif pot > bet > 200:
                    print("The maximum bet is $200")
                else:
                    return bet
        else:
            print("ERROR: This is not a valid input. Only integers accepted")
            sys.exit()
