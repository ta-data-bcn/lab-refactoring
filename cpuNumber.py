import random
import levels

def computer_number(level):
    number = random.randint( levels.levels[level][1], levels.levels[level][2] )
    tries = levels.levels[level][0]
    return (number, tries)
