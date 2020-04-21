#First of all, needed libraries are imported.

import random as random
from PIL import Image, ImageDraw, ImageFont


#A list of player will allow us to what player are we using the do an action o change the state of the game.


player = ['player_A', 'player_B', "unconquered"]

# How many available troops each player has.

player_A_available_troops = 0
player_B_available_troops = 0
available_troops = {"player_A":player_A_available_troops, "player_B":player_B_available_troops}

player_order = ['player_A', 'player_B']

#At the beginning, each continent is defined. They will have an unknown owner and an 0 troops in it.

#Africa = [player, 0]
#Oceania = [player, 0]
#Europa = [player, 0]
#Asia = [player, 0]
#North_America = [player, 0]
#South_America = [player, 0]
 
# Also, a list called "continents" have all continents previously defined.
# This list will have the values [name_of_the_continent, owner_player, number_of_troops_in_it].
# By default, at the beginning, all continents will have an owner called player[2] == 'unconquered'

continents = [['Africa', player,0], ['Asia', player,0], ['Europa', player, 0], ['North_America', player,0], ['South_America', player,0], ['Oceania', player,0]]
continents_tuple = ("Africa", "Asia", "Europa", "North_America", "South_America", "Oceania")


def turn_dice_roll(): # This function will roll dices at the beginning of the game to see who goes first.
    
    player_order=[]
    
    player_A = random.randrange(1,7) #This will work as a dice, going from 1 to 6, both included.
    player_B = random.randrange(1,7) #This will work as a dice, going from 1 to 6, both included.
    while player_A == player_B:
        player_A = random.randrange(1,6)
        player_B = random.randrange(1,6)
    
    if player_A > player_B:
        print(f"""Result of the player A: {player_A} 
        Result of the player B: {player_B} 
        Player A starts first""")
        player_order.extend(["player_A", "player_B"])
        return player_order
       #return modifies the value of the value, even if it was declared in the beginning.
         
    else:
        print(f"""Result of the player A: {player_A} 
        Result of the player B: {player_B} 
        Player B starts first""")
        player_order.extend(["player_B", "player_A"])
        return player_order
       #return modifies the value of the value, even if it was declared in the beginning.

        
#lets execute the function        
#turn_dice_roll()

# BIG REVEAL: if I dont associate a variable to the function, it wont change the value of player_order
# ths value, by default was "first A, then B" and it wouldn change in other functions even if we were
# recieving a "first B, then A". After storing the function in a variable, this change happens.
#player_order = turn_dice_roll()


def place_troops():

    continents_tuple = ("Africa", "Asia", "Europa", "North_America", "South_America", "Oceania")

    player = ['player_A', 'player_B', "unconquered"]

    continents = [['Africa', player,0], ['Asia', player,0], ['Europa', player, 0], ['North_America', player,0],
              ['South_America', player,0], ['Oceania', player,0]]
    
    
    available_troops = {"player_A":5, "player_B":5}

    continents_list = list(continents_tuple)
    print(continents_list)

    used_continents = []
    print("Now all of you have to place all your troops in different continents.")

    while available_troops["player_A"] != 0 and available_troops["player_B"] !=0:
            for player in player_order:

                if available_troops[player] == 0:
                    continue
                # Prints some info for the player
                print(f'It is your turn {player}, you have {available_troops[player]} troops available.')
                # inputs for both continent and quantity of troops in it
                continent_chosen = input(f"""In which continent do you want to place your troops?
                {continents_list}""")
                while continent_chosen in used_continents: #this prevents to repeat continents
                    continent_chosen = input(f"""That continent is already ocupied. 
                    Choose a continent in {continents_list}""")
                #a little check to prevent typing errors break the game.
                while continent_chosen not in continents_tuple: 
                    continent_chosen = input(f"""You had a mistake, type it correctly please.
                    {continents_list}""")
                #The well written continent is added to the list of used_continents
                used_continents.append(continent_chosen)
                continents_list.remove(continent_chosen)
                # the quantity of troops is chosen
                troops_quantity = int(input(f"And how many troops do you want to place? Remember you have {available_troops[player]}. "))
                while int(troops_quantity) > int(available_troops[player]): 
                    troops_quantity = input(f"""You had a mistake, type it correctly please.
                    Troops quantity can not be bigger than your available troops, which are {available_troops[player]}. """)
                #once the player has chosen a continent and a number of troops, the systems has to defined this change
                for a_continent in continents:
                    if a_continent[0] == continent_chosen:
                       # if a_continent[2] != 0: #this prevents conflicts. Only 1 player may be in a continent.
                       #     print("There are troops in this continente. Choose other.")
                        continents[continents.index(a_continent)][1] = [str(player)]
                        continents[continents.index(a_continent)][2] = [troops_quantity]
                        available_troops[player] -= int(troops_quantity)    
                        #print(available_troops[player]) # test print
                        #print(a_continent) # test print
                        #print(continents) # test print
    
    # a for loop to place "unconquered" in the unconquered continents.
    for a_continent in continents:
        if "unconquered" in a_continent[1]:
            continents[continents.index(a_continent)][1] = [str("unconquered")]
            continents[continents.index(a_continent)][2] = [0]
    
    print("Final state of continents before leaving this stage", continents)

    return continents

# doing this it is enough. The list continent will be updated.
#continents = place_troops()


#this function defines how many troops a player generates at the beginning of its turn.
# 

# the following lines are just for testing issues
#print(continents)
#continents = [['Africa', "player_A",0], ['Asia', "player_A",0], ['Europa', "player_A", 0], ['North_America', "player_A",0], ['South_America', "player_A",0], ['Oceania', "player_A",0]]
#player = 'player_A' # test variable


def generate_troops(player):
    player_A_available_troops = 0
    player_B_available_troops = 0
    continents_possessed = []
    
    #to make more manageable, the number of troops will be in dictionary, 
    #so it wont be affected by the orden or the players
    available_troops = {"player_A" : 0, "player_B" : 0}
    
    # print(f'Initial available troops for {player} are: ', available_troops[player]) # just a test print
    
    # We are going to evaluate the continents, to know if a continent is owned by a player
    # In that case, it will gain a +1 in "continents_possessed" variable. 
    # That number/2 will be the number of troops obtained at the beginning of the player's turn.
    for continent in continents:
        if player in continent[1][0]:
            continents_possessed.append(continent[0])
        #print(continents_possessed) #just test print
            
    print(f'{player} possesses {len(continents_possessed)} continents: {continents_possessed}')
    
    # every turn each player will obtain at least a new troop
 
    available_troops[player] = round(len(continents_possessed)/2)
    if available_troops[player] == 0:
        available_troops[player] = 1 
          
    print(f'Because of that (and because you will always get at least 1 troop) you recieved {available_troops[player]} troops.')


    return available_troops[player]

# Copy this line in the final Game
# available_troops[player] = generate_troops(player)

#print('the troops available for the player are', available_troops[player]) # test print

# the testing lines shows this program works


# This function controls the placements of troops.
# The main difference with the other one is that in the first the numbers of troops is always the same.
# In this one, it will be changing during each different turn and player.

# The function will be define for the "player" input.


# testing 'continents list'
#continents = [['Africa', ['player_B'], [5]], ['Asia', ['player_A'], [5]], ['Europa', ['unconquered'], 0], ['North_America', ['unconquered'], 0], ['South_America', ['unconquered'], 0], ['Oceania', ['unconquered'], 0]]


def place_troops_turn(player):
    
    # The following 2 lines are test variables to check the function.     
    #player = 'player_A' # Just a test variable
    #available_troops[player] = 3
 
    
    # This list reflects the continents owned by the player.
    # In this continents, the player will be able to place troops.
    # Also, doing so, it resets the status at the beginning of each turn
    # representing how the game board changes
    possible_continents = []
    
    for a_continent in continents:
        if a_continent[1][0] == player:
            possible_continents.append(a_continent[0])
    
    print(f'{player} you have to place your new {available_troops[player]} troopes in the following continents:', possible_continents)
   
    # 'available_troops' comes from the "generate_troops" function.
    
    while available_troops[player] != 0:
        
        # Inputs for both continent and quantity of troops in it.
        
        continent_chosen = input(f"""In which of your conquered continents do you want to place your troops?
        {possible_continents}""")         
   
              
        #a little check to prevent typing errors break the game.
        while continent_chosen not in possible_continents: 
            continent_chosen = input(f"""You had a mistake, type it correctly please.
            {possible_continents}""")
                    
        # The quantity of troops is chosen
        
        troops_quantity = int(input(f"And how many troops do you want to place? Remember you have {available_troops[player]}. "))
        while int(troops_quantity) > int(available_troops[player]): 
                troops_quantity = input(f"""You had a mistake, type it correctly please.
                Troops quantity can not be bigger than your available troops, which are {available_troops[player]}. """)
                
        #once the player has chosen a continent and a number of troops, the systems has to defined this change
        for a_continent in continents:
            if a_continent[0] == continent_chosen:
                continents[continents.index(a_continent)][2][0] = troops_quantity
                print(a_continent)
                available_troops[player] -= int(troops_quantity)
    
    #finally, the list 'continents' is returned, showing the state of the game
    return continents
    
 

 # 2 test lines to check the function
#place_troops_turn("player_A")  #test function

#continents = place_troops_turn("player_A")  
#print(continents)   #test print  

# We have to copy this in the final Game
# continents = place_troops_turn(player)


#This function will control the movements of the different troops.
#Only a movement for each player will be done in each turn. At least in this first version.

# testing 'continents list'
continents = [['Africa', ["player_A"],0], ['Asia', ["player_A"],0], ['Europa', ["player_A"], 0], ['North_America', ["player_A"],0], ['South_America', ["player_A"],0], ['Oceania', ["player_A"],0]]
#testing print before function
player = 'player_A' # testing variable

def moving_troops(player):
    
    # The following line are test variables to check the function.     
    player = 'player_A'

    #Since Earth is quite asymetrical not all continents will have the same possibilities.
    # Lets just define some relations.
    # In this tuples we will show the movement possibilities an army will have depending of its position.
    africa_mov = ('Europa', 'Asia', 'South_America', 'Oceania')
    asia_mov = ('Europa', 'North_America', 'Oceania', 'Africa')
    europa_mov = ('Asia', 'Africa', 'North_America')
    north_america_mov = ('Europa', 'South_America', 'Asia')
    south_america_mov = ('Africa', 'North_America', 'Oceania', 'Asia')
    oceania_mov = ('Africa', 'Asia', 'South_America')
    
    # This dictionary includes the relations between the continents and its possible movement paths.
    path_dict = {"Africa": africa_mov, "Asia": asia_mov, "Europa":europa_mov, "North_America":north_america_mov, 'South_America': south_america_mov, 'Oceania': oceania_mov}
    
    # Some rules explanation for the players.
    print(f"""It is your turn to move {player}. You will have only 1 movement and 3 possible option: 
    - Reinforce: To move troops from a controlled continent to another controlled continent.
    - Explore: To move your troops to an unconquered continent. You will capture it instantly.
    - Attack: try to conquere an enemy territory attacking it.
    - Do nothing: the player does not move any troop and finishes the turn.
    
    When moving your troops, independly of the result of the movement, 
    a troop will have to remain in the original continent.""")
    
    
    
    
    #First, the possible movements are defined. Continents has been updated after placing the new troops.
    possible_continents = []
    
    # a for loop to determine (and print) the continents where you have troops so you can move them
    for a_continent in continents:
        if a_continent[1] == player:
            possible_continents.append(a_continent)
    
    # Explanations for the player.
    initial_decision = input("""Do you want to move any of your troops? You can reinforce continents, 
    discover continents, attack or do nothing. 
    - If you type Yes, you will do something.
    - If you type No, you will do nothing and your turn will end.""")
    
    # A loop to control we are recieving a valid input.
    while [(initial_decision != "Yes") or (initial_decision != "No")]:
            initial_decision = input(f"""You had a mistake, type Yes or No. 
            {possible_continents}""")
    
    #A quick if/else to finished the turn if the player chooses to do nothing.
    if initial_decision == "No":
        print("You pass your turn.")
        
    else:
        #Input, where the player, decides which troops is moving
        chosen_continent = input(f"""The possible continents, where you have troops, are: {possible_continents}
        What do you choose? The possible paths will be shown after your correct selection.""") # A feedback print.

        # A loop to control we are recieving a valid input.
        while chosen_continent not in possible_continents:
            chosen_continent = input(f"""You had a mistake, type it correctly please.
                {possible_continents}""")
            
        print(f"""You have chosen to move the troops in {chosen_continent}. 
        You can move these troops to the following continents: {path_dict[chosen_continent]}""")



        print(continents_and_troops)    
        #input("""What troopes do you want to move? You have this troopes in these continents:
        #""")
        
    #evaluation: what are you going to find?
    for continent in continents:
        if chosen_continent == continent[0]: 
            if continent[1][0] == player:
                #reinforce function
                print('Reinforce')
            elif continent[1][0] == "unconquered":
                #discover function
                print('Discover')
                print("This land hasn't been conquered yet so you able to conquer it without a fight.")
                conquering_troops = input(f"""How many troops will you place in this place? 
                Remember that at least you have to leave 1 troop in the continent of origin. 
                Considering this, you have {continent[2][0]} available troops""")
            
            else:
                #attack function
                print('Attack')


    
    
#movement = moving_troops("player_A")


'''def discover():

This function allows the player to conquered
non-ocuppied lands.
'''


# This function analize if a player has conquered all the continents. 
# Only a player is be able to stay in a continent at the same time, so if a player is in all continents,
# it means that player conquered all continents and won the game.


# just to make some experiments, i will paste here a 'continents' list with player_A as the winner
#continents = [['Africa', ["player_A"],0], ['Asia', ["player_A"],0], ['Europa', ["player_A"], 0], ['North_America', ["player_A"],0], ['South_America', ["player_A"],0], ['Oceania', ["player_A"],0]]


def evaluate_game(continents): 
    winner = ['player_A', 'player_B']
    player_A_counter = 0
    player_B_counter = 0
    for situation in continents:
        if situation[1][0] == "player_A":
            player_A_counter += 1
            #print(player_A_counter) #test print
        elif situation[1][0] == "player_B":
            player_B_counter += 1
            #print(player_B_counter) #test print
    if player_A_counter == len(continents):
        print('The winner of this game is: '+ str(winner[0])+'!!!')
        return winner[0]   
    
    elif player_B_counter == len(continents):
        print('The winner of this game is: '+ str(winner[1])+'!!!')
        return winner[1]

# Tested. The following line is not needed at all.
#evaluate_game(continents)

#This following lines must be included in the final program. But in this cell it will be hashed.
#final_winner = evaluate_game(continents)    

    
            
# This function must go in the end (or almost) of the code.
# Also, it will be repeated after each player finishes its turn.

#function tested. IT WORKS FINE

def print_map():
    # With this function you will be able to show the world map.
    # It will contain an image of the world (in a pretty "old style").
    # Also, you will see which player owns the continent (Player 1, Player 2 or Unconquered)
    # and the quantity of troops placed in it.

    # This library, Pillow, allow us to print and modify images.
    # If not at the beginning of the code, active the following line:
    #from PIL import Image, ImageDraw, ImageFont
    
    # create Image object with the input image
 
    image = Image.open('map_02.jpg')

    # initialise the drawing context with the image object as background
    draw = ImageDraw.Draw(image)

    # create font object with the font file and specify desired size
    font = ImageFont.truetype('Roboto-Bold.ttf', size=40)

    # coordinates
    coordinates = ((600, 450), (800, 200), (500, 250), (150, 200), (150, 500), (900, 600))

    # continents' name. Sample to make tests.
    continents = [['Africa', ['player_A'], [5]], ['Asia', ['player_B'], [5]], ['Europa', ['unconquered'], [0]], ['North_America', ['unconquered'], [0]], ['South_America', ['unconquered'], [0]], ['Oceania', ['unconquered'], [0]]]

    #color of the font:
    color = 'rgb(0,0,0)' # black color
    
    # Problem: the text must be a string. 
    # Consider that the number of troops is an integer and must be converted into a string.
    for continent in zip(continents,coordinates):
        #print(continent) #control print. Very useful. Use it when you find problems.
        draw.text((continent[1][0], continent[1][1]), continent[0][0], fill=color, font=font) #this line prints the Continent
        draw.text((continent[1][0], continent[1][1] + 40), continent[0][1][0], fill=color, font=font) #this line prints the Player
        draw.text((continent[1][0], continent[1][1] + 80), str(continent[0][2][0]) + ' troops', fill=color, font=font)#this line prints the Troops

    # save the edited image 
    image.save('map_02_with_texts.jpg')

    return image

#execute the image:
#image

#print_map()

#First of all, needed libraries are imported.

import random as random

#A list of player will allow us to what player are we using the do an action o change the state of the game.


player = ['player_A', 'player_B', "unconquered"]

# How many available troops each player has.

player_A_available_troops = 0
player_B_available_troops = 0
available_troops = {"player_A":player_A_available_troops, "player_B":player_B_available_troops}

player_order = ['player_A', 'player_B']

#At the beginning, each continent is defined. They will have an unknown owner and an 0 troops in it.

#Africa = [player, 0]
#Oceania = [player, 0]
#Europa = [player, 0]
#Asia = [player, 0]
#North_America = [player, 0]
#South_America = [player, 0]
 
# Also, a list called "continents" have all continents previously defined.
# This list will have the values [name_of_the_continent, owner_player, number_of_troops_in_it].
# By default, at the beginning, all continents will have an owner called player[2] == 'unconquered'

continents = [['Africa', player,0], ['Asia', player,0], ['Europa', player, 0], ['North_America', player,0], ['South_America', player,0], ['Oceania', player,0]]
continents_tuple = ("Africa", "Asia", "Europa", "North_America", "South_America", "Oceania")

# The dices are roles. This will determine the order or players.
# turn_dice_roll() #this variable is asigned
player_order = turn_dice_roll()



print("""______________________________
                                 """) #just to make more the game more readeable

#now, time to place our troops
continents = place_troops()

#lets print the map for the first time to see the initial setup
print_map()

print("""______________________________
                                 """) #just to make more the game more readeable

#constant evaluation of the game
final_winner = evaluate_game(continents)    


# while there is not a winner keep going round after round

while final_winner != 'player_A' or final_winner != 'player_B':
    for player in player_order:
        
        print(f"It is {player} turn.")
        print("""
        --------- Troops Generation Phase ---------
                                 """) #just to make more the game more readeable
        
        available_troops[player] = generate_troops(player)
        
        print("""
        --------- Placing New Troops Phase ---------
                                 """) #just to make more the game more readeable
        
        continents = place_troops_turn(player) 
        
        print("""______________________________
                                 """) #just to make more the game more readeable
        
        print(f"End of {player} turn.")
        
        print("""______________________________
                                 """) #just to make more the game more readeable
        
        #Always check at the end of each turn if a player won.
        #If you dont do that the while loop wont ever break.
        
        final_winner = evaluate_game(continents)
        
        
        
        #the following will gently finish the game:
        final_winner = 'player_A'
        break
        
        
print('''THANK YOU FOR PLAYING THIS ALPHA VERSION!
MORE STUFF WILL BE READY IN THE FUTURE.
INCOMMING FEATURES:
- MAPS
- MOVEMENTS
- AI PLAYER
- MULTIPLE PLAYERS
- MULTIPLE AI/HUMAN PLAYERS

Any suggestion of feedback will be appreciated.
Thank you again.''')
        