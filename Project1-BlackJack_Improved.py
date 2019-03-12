# Note: I'm considering and infinite deck of cards
import random
import re
import sys
import time
from deck_values import deck_values
from pot import money_on_the_table

#The player places the bet at the beginning of each round
def bet_placing(pot):
    bet = 0
    while (bet < 5) or (bet > 200):
        bet = input("How much money do you want to bet on this round?. The maximum bet is $200 and the minimum bet is $5\n")
        if re.findall(r'(?<!\.)\b[0-9]+\b(?!\.)',bet):
            bet = int(bet)
            if bet > pot:
                print(f"You don't have that much, your current pot is ${pot}")
                bet = 0
            else:
                if bet < 5:
                    print("The minimum bet is $5")
                elif bet > 200 and bet < pot:
                    print("The maximum bet is $200")
                else:
                    return(bet)
        else:
            print("ERROR: This is not a valid input. Only integers accepted")
            sys.exit()
        
#The dealer deals the initial hands for a given deck. Retuns a tuple(?) with 2 lists, 2 items each, the player's hand and the dealer's hand
#WARNING when printing the result, the second card of the dealer's hand should not be shown
def deal_cards(deck):
    player_hand = [random.choice(deck) for x in range(2)]
    dealer_hand = [random.choice(deck) for x in range(2)]
    return player_hand, dealer_hand

#The player chooses what to do
def player_action(values):
    options = ["hit","pass"]
    player_choice = ""
    print("Your hand is",player_hand,"You are now at",hand_sum(player_hand,values))
    while player_choice not in options:
        player_choice = str(input(f"You can {options}, what would you like to do?\n"))
    return player_choice

#We calculate the sum of a hand. Needs a list and a dictionary
def hand_sum(hand,values):
    total = 0
    for card in hand:
        total += values[card]
    return total

#We ask if the player wants to keep playing
def keep_playing():
    if pot >= 5:
        keep = input("Do you want to keep playing Y/N ")
        while keep not in ['Y','N']:
            keep = input("Do you want to keep playing Y/N ")
        return keep == 'Y'
    else:
        print("You don't have enough chips on your pot :(")
        return False
    
#Build the game:
#Ask the player how much money he wants to put in the pot
pot = money_on_the_table()

#We create the deck
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#We create a loop for each round
give_me_more = True

while give_me_more:
    
    #We ask the player to place a bet for the current round
    print(f'You currently have ${pot} on your pot')
    bet = bet_placing(pot)
    player_busted = False
    dealer_busted = False

    #We deal the cards and display the current status
    print()
    dealing = ["Dealing...","...","...","..."]
    for line in dealing:
        print (line,)
        time.sleep(0.2)
    player_hand = deal_cards(deck)[0]
    dealer_hand = deal_cards(deck)[1]
    print("\nThe dealer's hand is:",dealer_hand[0],"[X]")

    #We check if the player holds a couple of A's (only hand of 2 cards higher than 21)
    player_two_as_in_hand = False
    player_sum = hand_sum(player_hand,deck_values(player_two_as_in_hand))

    if player_sum > 21:
        player_two_as_in_hand = True
        player_sum = hand_sum(player_hand,deck_values(player_two_as_in_hand))

    #We give the player the choice to take action
    time.sleep(1)
    if player_two_as_in_hand == True:
        action = player_action(deck_values(player_two_as_in_hand))
    else:
        action = player_action(deck_values(player_two_as_in_hand))

    while action == "hit":
        player_hand.append(random.choice(deck))
        
        if player_two_as_in_hand == False:
            player_sum = hand_sum(player_hand,deck_values(player_two_as_in_hand))
        else:
            player_sum = hand_sum(player_hand,deck_values(player_two_as_in_hand))
                
        if player_sum > 21 and 'A' not in player_hand:
            print(player_hand,"\nYou are now at",player_sum,"\nBusted!")
            action = "pass"
            player_busted = True
        elif player_sum > 21 and'A' in player_hand:
            player_sum = hand_sum(player_hand,deck_values(player_two_as_in_hand))
            if player_sum > 21:
                print(player_hand,"\nYou are now at",player_sum,"\nBusted!")
                action = "pass"
                player_busted = True
            else:
                action = player_action(deck_values(player_two_as_in_hand))
        elif player_two_as_in_hand:
            action = player_action(deck_values(player_two_as_in_hand))
        else:
            action = player_action(deck_values(player_two_as_in_hand))

    #Dealer's play
    dealer_sum = hand_sum(dealer_hand,deck_values(player_two_as_in_hand))
    #We check if the dealer holds a couple of A's (only hand of 2 cards higher than 21)
    dealer_two_as_in_hand = False
    if dealer_sum > 21:
        dealer_sum = hand_sum(dealer_hand,deck_values(player_two_as_in_hand))
        dealer_two_as_in_hand = True
    
    print("The dealer's hand is:",dealer_hand)

    while (dealer_sum < 17) and (player_busted == False):
        dealer_hand.append(random.choice(deck))
        
        if dealer_two_as_in_hand == True:
            dealer_sum = hand_sum(dealer_hand,deck_values(player_two_as_in_hand))
        else:
            dealer_sum = hand_sum(dealer_hand,deck_values(player_two_as_in_hand))
        
        if dealer_sum > 21 and 'A' not in dealer_hand:
            print("The dealer's hand is:",dealer_hand,"\nDealer is busted")
            dealer_busted = True
        elif dealer_sum > 21 and 'A' in dealer_hand:
            dealer_sum = hand_sum(dealer_hand,deck_values(player_two_as_in_hand))
            if dealer_sum > 21:
                print("The dealer's hand is:",dealer_hand,"\nDealer is busted!")
                dealer_busted = True
        else:
            print("The dealer's hand is:",dealer_hand,"\nWith a total score of",dealer_sum)

    #We settle the game and update the pot
    time.sleep(1)
    if player_busted:
        pot = pot - bet
        print(f"The dealer wins\n Your remaining pot is ${pot}")
    elif dealer_busted:
        pot = pot + bet
        print(f"You win!\n You have now ${pot} in your pot")
    else:
        if dealer_sum == 21 and player_sum == 21:
            if 'A' in dealer_hand not in player_hand:
                pot = pot - bet
                print(f"The dealer wins\n Your remaining pot is ${pot}")
            elif 'A' in player_hand not in dealer_hand:
                pot = pot + bet
                print(f"You win!\n You have now ${pot} in your pot")
            else:
                print("It's a split")
        else:
            if dealer_sum > player_sum:
                pot = pot - bet
                print(f"The dealer wins\n Your remaining pot is ${pot}")
            elif dealer_sum < player_sum:
                pot = pot + bet
                print(f"You win!\n You have now ${pot} in your pot")
            else:
                print(f"It's a split\n You have now ${pot} in your pot")

    give_me_more = keep_playing()


# In[ ]:




