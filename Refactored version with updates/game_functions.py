import random

coloured_balls = ["green", "yellow", "white", "black", "orange", "red", "purple", "blue"]
#functions to be imported
def random_cpu():
    import random
    """function randomly chooses a combination of 4 coloured balls for the computer ie. the Mastercode
    
    @Input : random function generates randomly a 4 coloured ball combination
    @Output : generates the MasterCode for the game to be cracked by the player"""
    
    return random.choices(coloured_balls, k=4)

def player_select():
    """Each round - ask the player to make a 4 coloured choice
    
    @Input : the player has to input 4 coloured ball
    @Output : 4 ball combination"""
    
    print("choose 4 coloured balls (among green, yellow, white, black, orange, red, purple, blue")
    print("Do or Do not. There is no try. good luck padawan")
    
    player_input_ball_list = []
    
    for i in range(4):
        player_input_ball = input()
        while player_input_ball not in coloured_balls:
            player_input_ball = input("\n Wait a minute ! please choose a colour among the 8 coloured balls. \
                                      i.e. green, yellow, white, black, orange,red,purple,blue. \
                                      No more, No less \n")
        player_input_ball_list.append(player_input_ball)
    
    print("\ncongrats, you have chosen", player_input_ball_list, "a wise choice \n")
    
    return player_input_ball_list

def each_round_check(computer_Mastercode,player_guess):
    """check whether the player has guessed correctly the Master code
    
    @Input : round's player guess
    @Output : Computer gives feedback whether the player's getting close or not"""
    
    comparing_list_temp = []       
    
    for i,j in zip(computer_Mastercode,player_guess):
        if i == j:
            print("That ball",j,"is in the right place")
        elif j in computer_Mastercode:
            comparing_list_temp.append(j)
        else:
            print("not even close mate ! There is no",j,"in my code")
    if comparing_list_temp != []:
        print("\nThose items", comparing_list_temp, "are in the Mastercode but in different location")

def finale_result(player_guess,computer_Mastercode):
    """Check the finale result of the game
    
    @Input : each round check whether the player is right OR after 10 rounds, the game ends
    @Output : gives the name of the winner - the Codebreaker OR the Mastercode.
    There is no middle ground"""
    
    if player_guess == computer_Mastercode:
        print("\ncongrats, you have broken the code, you're a Grand Master !")
    else:
        print("I knew you did not have what it takes to break the Mastercode. Try again, my very young padawan")      