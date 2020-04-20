import random
import levels as lvl

def computer_number(level):
    number = random.randint( lvl.levels[level][1], lvl.levels[level][2] )
    tries = lvl.levels[level][0]
    return (number, tries)
