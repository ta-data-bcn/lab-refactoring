def money_on_the_table():
    """
    The player has a total amount of money (pot), defined at the beginning of the game. The minimum pot is 5.

    :return: pot (int)
    """
    pot = 0
    while pot < 5:
        pot = input("How much money do you want to bet on this table. The minimum bet is $5\n")
        if re.findall(r'(?<!\.)\b[0-9]+\b(?!\.)',pot):
            pot = int(pot)
        else:
            print("ERROR: This is not a valid input. Only integers accepted")
            sys.exit()
    return(pot)