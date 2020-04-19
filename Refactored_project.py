#!/usr/bin/env python
# coding: utf-8

# # 21 Blackjack

# #### Import the random library to take random cards

# In[ ]:


import random as r


# ####  Introduce the game

# In[ ]:


def greeting():
    print("Hi there! Welcome to 21 Blackjack.\n")


# #### Define number & name of the players

# In[ ]:


def players():
    print("First of all, let's see how are we going to play today")
    nPlayers = input("How many of you want to play? ")
    while not nPlayers.isdigit(): #if the input is not a digit, keep asking
         nPlayers = input("Type in a number? PLease... \n")
    nPlayers = int(nPlayers) #casting the input into an int
    playersNames = []
    currentPlayer = ""
    for n in range(nPlayers): #iterate through the number of players in order to get their names
        currentPlayer = input(f'What is the name of the player number {n + 1}? ')
        playersNames.append(currentPlayer) #append the name of the players to a list
        print(f'Hello {currentPlayer}!, nice to meet you\n')
    playersDict = {player:{'Cards':[],"Score":0} for player in playersNames} #creating a players to store cards & their score
    print("Enough with the small talk, let's begin!\n")
    playersDict.update({"Dealer": {'Cards':[],"Score":0}}) #add the Dealer to the dict
    return playersDict


# #### Define how many push ups is each player betting

# def players_bets():
#     players_bets = []
#     for player in players_dict.keys():
#         if player != 'Dealer':
#             current_player_bet = input(f'{player}, how many push ups are you going to bet in this hand? ')
#             players_bets.append(current_player_bet)
#     return players_bets

# #### Create a deck (List with the name of the cards and it's value)

# In[ ]:


def create_deck():
    suits = ['Spades', ' Hearts', 'Diamonds', 'Clubs']
    cardsNumbers = [n+1 for n in range(10)] + ['Jack', 'Queen', 'King']
    cardsValue = [value if type(value) == int else 10 for value in cardsNumbers] #create a list with the cards value
    deck = [[str(c)+ f' of {s}',v] for s in suits for c,v in zip(cardsNumbers,cardsValue)] #create a deck with cards name and value
    return deck


# #### Take n cards from the deck

# In[ ]:


def take_cards(n): #Select n cards from the deck
    cards = []
    for i in range(n): #number of cards to take
        card = deck[r.sample(range(len(deck)),1)[0]] #take a random card/s from the deck
        deck.remove(card) #take the card/s out of the deck list
        cards.append(card) #create a list with the taken cards
    return cards


# #### Calculate the score of a list of cards

# In[ ]:


def calculate_score(cardList): #list of cards given to a player
    score = 0
    for i in range(len(cardList)): #iterate through the list of cards
        if cardList[i][1] == 1 or cardList[i][1] == 11: #check if its an ace, the player can change the value at any time
            ace_value = int(input(f'Do you want your card to be a 1 or a 11? Your current score is {score}, choose wisely \n'))
            while ace_value not in [1,11]: #checking the input
                ace_value = int(input("It's not that hard :D, type 1 or 11 \n"))
            cardList[i][1] = ace_value #assigning the value choosen by the player to the list
        score += cardList[i][1] 
    return score


# #### Print the status of a player

# In[ ]:


def status(player): #name of the player
    print(player, 'your cards are ',', '.join([c[0] for c in playersDict[player]['Cards']]), 'and your score is', playersDict[player]['Score'],'\n')
    #joining the name of the cards and its score in the player dictionary


# #### Assign n cards to a player

# In[ ]:


def give_cards(n,player): #number of cards to give and to which player
    playersDict[player]['Cards'] += take_cards(n) #call take cards function and adding it to the players dict
    print(player, 'your cards are ',', '.join([c[0] for c in playersDict[player]['Cards']])) #printing their cards
    playersDict[player]['Score'] = calculate_score(playersDict[player]['Cards']) #call calculate score and updated in the dict
    print('And your current score is ',  playersDict[player]['Score'],"\n") #print their score


# #### Variable to check if the players want to keep playing

# In[ ]:


keepPlaying = 'Yes' #creating a variable to check if they want to keep playing once the hand is over


# ### Main Blackjack game

# In[ ]:


greeting()

playersDict = players()

while keepPlaying.capitalize() == 'Yes': 
    deck = create_deck()
    playersDict = {player:{'Cards':[],"Score":0} for player in playersDict.keys()} #reset the dict to 0 to restart the game

    for player in playersDict.keys(): #first hand, give 2 cards to every player
        give_cards(2, player)

    for player in playersDict.keys(): #see if the players want to hit or stand
        moves = ['hit','stand']
        stand = True
        while playersDict[player]['Score'] < 21 and stand: #check if the score is over 21                
            move = input(player + ' Do you hit or stand? your current score is ' + str(playersDict[player]['Score']) + ' \n')
            while move.lower() not in moves:
                move = input("Come on... hit or stand? ")
            if move.lower() == 'hit':
                give_cards(1,player)
            else:
                print('Better safe than sorry, your final score is ' + str(playersDict[player]['Score']) + ' \n')
                stand = False

        if playersDict[player]['Score'] == 21: #check if its Blackjack
            print('Blackjack! Congratulations, ' + player + '!,hope the dealer does not hit it too \n')
        elif calculate_score(playersDict[player]['Cards']) > 21: # if its higher, the player loses
            print('Your score is over 21... sorry, you lost \n')
    
    dealerScore = playersDict['Dealer']['Score'] #store the dealers score in a variable
    if dealerScore == 21: #if the dealer hits a Blackjack, wins
        print('The Delaer hit 21... sorry, but you lost ')
        print([status(player) for player in playersDict.keys()])
    else:
        for player in playersDict.keys(): #check the players scores with the dealer score
            if player != 'Dealer':
                if playersDict[player]['Score'] > 21:
                    print(f'{player}, your score is over 21... sorry, you lost')
                    print (status(player))
                elif playersDict[player]['Score'] > dealerScore or dealerScore > 21:
                    print(f'Congratulations {player} you beat the Dealer')
                    print(status(player))
                else:
                    print(f'Sorry {player} the Dealers hand beats yours...')
                    print(status(player))
    
    keepPlaying = input('If you want to keep playing, say yes! \n') #check if the players want to keep playing
    if keepPlaying != 'yes':
        print('\nThanks for playing! Hope to see you again!')
    else:
        continue
    
    
    

