# Note: I'm considering and infinite deck of cards
import random
import time
from deck_values import deck_values, hand_sum
from pot import define_pot
from bet_placing import place_bet
from cards_dealing import deal_cards
from player_action import decide_player_action, decide_keep_playing


# Build the game:
# Ask the player how much money he wants to put in the pot
pot = define_pot()

#We create the deck
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#We create a loop for each round
give_me_more = True

while give_me_more:
    
    #We ask the player to place a bet for the current round
    print(f'You currently have ${pot} on your pot')
    bet = place_bet(pot)
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
        action = decide_player_action(player_hand, player_sum)
    else:
        action = decide_player_action(player_hand, player_sum)

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
                action = decide_player_action(player_hand, player_sum)
        elif player_two_as_in_hand:
            action = decide_player_action(player_hand, player_sum)
        else:
            action = decide_player_action(player_hand, player_sum)

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

    give_me_more = decide_keep_playing(pot)



