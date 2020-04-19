
# Input who's begining the game
# Error handling on typos checked (case insensitive and strip spaces)
def input_first_choice():
    
    firstChoice = input("Who will begin the game: Cpu or You? (Type: cpu or me, case not-sensitive) ")

    while True:
        # check input
        if firstChoice.lower().strip(" ") in ['cpu','me']:
            return firstChoice.lower().strip(" ")
        else:
            firstChoice = input("Please type cpu or me (case not-sensitive)!")