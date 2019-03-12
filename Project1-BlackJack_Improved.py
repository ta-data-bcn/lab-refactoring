# Note: I'm considering and infinite deck of cards
import random
import time
from deck_values import hand_sum
from pot import define_pot
from bet_placing import place_bet
from cards_dealing import deal_cards
from player_action import decide_player_action, decide_keep_playing


# Definition of global variables
pot = define_pot()
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
give_me_more = True

while give_me_more:

    # We ask the player to place a bet for the current round
    print(f'You currently have ${pot} on your pot')
    bet = place_bet(pot)
    player_busted = False
    dealer_busted = False

    # We deal the cards and display the current status
    player_hand = deal_cards(deck)[0]
    dealer_hand = deal_cards(deck)[1]
    print("\nThe dealer's hand is:", dealer_hand[0],"[X]")

    # We check if the player holds a couple of A's (only hand of 2 cards higher than 21)
    player_ace_as_one = False
    player_sum = hand_sum(player_hand, player_ace_as_one)

    if player_sum > 21:
        player_ace_as_one = True
        player_sum = hand_sum(player_hand, player_ace_as_one)

    # We give the player the choice to take action
    #TODO include timespleep in function decide player action
    time.sleep(1)
    action = decide_player_action(player_hand, player_sum)

    while action == "hit":
        player_hand.append(random.choice(deck))

        # Update player sum
        player_sum = hand_sum(player_hand, player_ace_as_one)

        #TODO summarise this into a settle funtion
        if player_sum > 21 and 'A' not in player_hand:
            print(player_hand, "\nYou are now at", player_sum,"\nBusted!")
            action = "pass"
            player_busted = True
        elif player_sum > 21 and'A' in player_hand:
            player_ace_as_one = True
            player_sum = hand_sum(player_hand, player_ace_as_one)
            if player_sum > 21:
                print(player_hand,"\nYou are now at",player_sum,"\nBusted!")
                action = "pass"
                player_busted = True
            else:
                action = decide_player_action(player_hand, player_sum)
        elif player_ace_as_one:
            action = decide_player_action(player_hand, player_sum)
        else:
            action = decide_player_action(player_hand, player_sum)

    # Dealer's play
    dealer_ace_as_one = False
    dealer_sum = hand_sum(dealer_hand, dealer_ace_as_one)

    # Corner case: We check if the dealer holds a couple of A's (only hand of 2 cards higher than 21)
    if dealer_sum > 21:
        dealer_ace_as_one = True
        dealer_sum = hand_sum(dealer_hand, dealer_ace_as_one)

    print("The dealer's hand is:", dealer_hand)

    while (dealer_sum < 17) and (not player_busted):
        #TODO add one card should be a function of the dealing library, check also for player
        dealer_hand.append(random.choice(deck))

        dealer_sum = hand_sum(dealer_hand, dealer_ace_as_one)

        #TODO summarise this into a settle function, also in player
        if dealer_sum > 21 and 'A' not in dealer_hand:
            print("The dealer's hand is:",dealer_hand,"\nDealer is busted")
            dealer_busted = True
        elif dealer_sum > 21 and 'A' in dealer_hand:
            dealer_sum = hand_sum(dealer_hand, dealer_ace_as_one)
            if dealer_sum > 21:
                print("The dealer's hand is:",dealer_hand,"\nDealer is busted!")
                dealer_busted = True
        else:
            print("The dealer's hand is:",dealer_hand,"\nWith a total score of",dealer_sum)

    #TODO all this should be in the settle library

    # We settle the game and update the pot
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



