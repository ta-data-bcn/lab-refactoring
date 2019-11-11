#!/usr/bin/env python
# coding: utf-8

# In[3]:


######################################
## Welcome to Mastermind - The Game ##
# Below you will find the modules,   #
# variables, lists and functions     #
# required to run a game of          #
# Mastermind                         #
######################################

### MODULES TO IMPORT ###
import random

### DICTIONARIES

colour_lookup_words = {
    "R": "\033[0;37;41m RED \033[0m",
    "G": "\033[0;37;42m GREEN \033[0m",
    "Y": "\033[0;30;43m YELLOW \033[0m",
    "B": "\033[0;37;44m BLUE \033[0m",
    "M": "\033[0;37;45m MAGENTA \033[0m"
}

### VARS & Lists

code_to_crack = []
colour_letters = ["R","G","Y","B","M"]
count_black = 0
count_white = 0
game_round = 0
n_rounds= 5
player_guess= []
won_yet = False


### FUNCTIONS

def game_start():
    """Initiates the game by clearing any lists from previous guesses, 
    diplaying welcome message and generating the secret code.
    REFERENCED FUNCTIONS
    game_reset
    display_welcome_message
    cpu_code_gen
    """
    game_reset()
    display_welcome_message()
    cpu_code_gen()
    
def game_reset():
    """Simply resets all variables and lists ready for the next game
    REFERENCED FUNCTIONS
    nil
    """    
    global code_to_crack 
    global count_black 
    global count_white 
    global game_round
    global player_guess
    global rounds
    code_to_crack = []
    count_black = 0
    count_white = 0
    game_round = 0
    player_guess= []
    rounds = 0
    
def display_welcome_message():
    """Display a welcome message that explains the rules of the game and required inputs (used later on).
    No function purpose other than to print
    """
    print ('''inert long test with \n here - use enter as a carraige return ....'''
    print ("######################################################## ")
    print ("######## Welcome to the game of Mastermind 2019 ######## ")
    print ("######################################################## ")
    print ("\nIn this game you'll be playing against the computer who will create a combination of 3 from a pool of 5 colours. The computer can repeat the colour selection.")
    print ("For example the computer could pick RED RED YELLOW or GREEN GREEN GREEN")
    print ("You will have 5 attempts to try and guess the correct colour and position of the computers combination")
    print (f"Remeber the options are \033[0;37;41m [R]ED \033[0;37;42m [G]REEN \033[0;30;43m [Y]ELLOW \033[0;37;44m [B]LUE \033[0;37;45m [M]AGENTA \033[0m" )
    print ("GOOD LUCK | BUENA SUERTA \n \n")

def cpu_code_gen():
    """Generate a secret 'code' which is a 
    combination of 3 elements from a list 
    (which represent the first letter of colours).
    The letter (colour) seleted by computer can be repeated.
    Using a for loop to count out the 3 colours required (via range).
    REFERENCED FUNCTIONS
    nil
    """
    global code_to_crack
    code_to_crack = []
    for i in range(0,3):
        code_to_crack.append(random.choice(colour_letters))
    #return print(code_to_crack)

def init_user_input():
    """Displays the text to ask user for their three colour guesses.
    Utilises the player_guess_entry function for error validation.
    After successful input this funtion then displays 
    the colour choice back to the user before initiating the assessment_of_round function
    REFERENCED FUNCTIONS
    player_guess_entry
    assessment_of_round
    """
    global game_round
    global player_guess
    for i in range(1,4):
        player_guess_entry(f"Enter your guess for POSITION {i} : ")
    try:
        print(f"Your combination for this round is {colour_lookup_words[player_guess[0]]} {colour_lookup_words[player_guess[1]]} {colour_lookup_words[player_guess[2]]}\033[0m")
    except:
        print(f"You didn't enter your values properly!")
        player_guess=[]
        for i in range(1,4):
            player_guess_entry(f"Enter your guess for POSITION {i} : ")
    game_round += 1
    assessment_of_round()

def player_guess_entry(text_to_ask):
    """Error validation for each of the letter entered by the user during Fn: init_user_input
    REFERENCED FUNCTIONS
    nil
    """
    global player_guess
    #try with while -n when you get the erro \r for just return - look at feedback and input ito code.
           try:
        guess_var = input(f"{text_to_ask}")
    except:
        print("Remember to use a single character [R]ed [G]reen [Y]ellow [B]lue [M]agenta")
    if guess_var not in str(colour_letters) or guess_var == "":
        print("Remember to use a single character [R]ed [G]reen [Y]ellow [B]lue [M]agenta")
    else:
        player_guess.append(guess_var.upper())

def assessment_of_round():
    """Assesses user's guess to determine 1 of 3 scenarios. Win, 
    Correct colour in an incorrect position (+1 white)
    Correct colour in a correct position (+1 black)
    REFERENCED FUNCTIONS
    assessment_of_player_peg
    peg_score_so_far
    """
    global player_guess
    global code_to_crack
    global won_yet
    if player_guess == code_to_crack:
        print("WINNER!!!")
        won_yet = True
        game_over()
    else:
        for i in range(0,3):
            assessment_of_player_peg(i)
        peg_score_so_far()
        round_reset()
        
def assessment_of_player_peg(position):
    """Assesses user's guess to determine 1 of 3 scenarios. Win, 
    Correct colour in an incorrect position (+1 white)
    Correct colour in a correct position (+1 black)
    REFERENCED FUNCTIONS
    nil
    """
    global count_white
    global count_black
    if player_guess[position] == code_to_crack[position]:
        count_black += 1
    elif player_guess[position] in code_to_crack:
        count_white += 1


def peg_score_so_far():
    """Prints the current summary of pegs scored through guess(es) so far.
    REFERENCED FUNCTIONS
    nil
    """
    global count_white
    global count_black
    return print (f"This guess scored you {count_white} white pegs and {count_black} black pegs. Keep going!")
    
def round_reset():
    """Simply resets all variables and lists ready for the next round
    REFERENCED FUNCTIONS
    nil
    """
    global player_guess
    player_guess = []
        
def game_over():
    """Prints a game over message 
    and asks if player wants to play 
    again, if so starts from the top
    REFERENCED FUNCTIONS
    game_start
    """
    print("Game over! Thanks for playing")
    start_again = input(f"Do you want to start again? (Y/N) ")
    if start_again == "Y":
        game_start()
    else:
        exit()


# In[ ]:


# the game is started here
game_start()
while game_round < 5 or won_yet is not True:
    init_user_input()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:









