
import random
from Soldier_and_Dice_functions import *


if __name__ == '__main__':
    # Setup:
    play = True
    while play:
        attack, defend = setup_armies()
        fight(attack, defend)
        play = yes_or_no('Do you want to play again?')

# Added the option to play indefinitely

