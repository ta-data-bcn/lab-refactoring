# Before starting, I recommend to look the other files in order to understand the game itself.

# The MAIN game is HERE

#variable and imports
from Functions import shuffle as s
from Functions import Change_A as ca
from Functions import money_player as mp
from Functions import opcions_game as og
from Functions import accion_game as ag
import re
import random
deck = ['A',2,3,4,5,6,7,8,9,10,10,10]*4
random.shuffle(deck)
bet=30
bet_in_table=60
money=0
playing="Yes"

#### Starting the game. In the game, the oficial bet is 30.

print ("\n Welcome to 21 Blackjack")
print ('''\n You are going to play against the dealer and each round you are going to bet the amount 
    you want until you do not have more money or the dealer has lose it everything. Be careful, you 
    win whit a Blackjack(21) or a hand higher than the dealer one. The dealer DOES NOT ACCEPT ERRORS,
     you have only chance. ''')

##### Function for inserting the quantity you want to play in the game.

money = mp.money_player(money)
    
# Loop the game keep running            
while playing == "Yes":
    
    if money == 'error':
        playing =='No'
        break
        
# The players get the cards they obtain from shuffleing and changing the values of any As they have.   

    hand_player = s.shuffle_card(deck)
    hand_dealer = s.shuffle_card(deck)

    hand_player = ca.change_A(hand_player, hand_dealer )[0]
    hand_dealer = ca.change_A(hand_player, hand_dealer )[1]    
     
    
    print(f"\n You have in hand {hand_player} with a total of {sum(hand_player)} ")
    
    print(f"\n The dealer has in hand {hand_dealer[0]} and the other covert ")


#### Calling the function of accion which make the player choose what he wants to do and show the result 
#### which is inside the opcions file 

    money = ag.accion( deck, money , bet , bet_in_table , hand_player , hand_dealer )

#function of accion again

    
    playing = input(f"\n You have {money} dollars. Do you want to keep playing? Answers with [Yes] or [No]."     )
    
    while playing != "Yes" and playing != "No":

        playing = input("\n You must answer with Yes or No, if you want to play or not.   ")

    if money > 300:
        print ("\n The dealer catch you counting. They quick you out of the casino.")
        money = 0
        playing=="No"
    if playing == "No":
        print (f"\n Thank you for playing Blackjack. You leave with {money} dollars")


