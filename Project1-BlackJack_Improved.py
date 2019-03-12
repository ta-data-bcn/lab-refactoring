# Note: I'm considering and infinite deck of cards
from deck_values import hand_sum
from pot import define_pot
from bet_placing import place_bet
from cards_dealing import deal_cards, deal_one
from player_action import decide_player_action, decide_keep_playing
import settle as stl

# Definition of global variables
pot = define_pot()
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
give_me_more = True

while give_me_more:

    # We ask the player to place a bet for the current round
    print(f'You currently have ${pot} on your pot')
    bet = place_bet(pot)

    # Define the status of the player [busted, sum of hand, hand, action] and the dealer [busted, sum of hand, hand]
    player_status = [False, 0, [], "pass"]
    dealer_status = [False, 0, []]

    # We deal the cards and display the current status
    player_status[2] = deal_cards(deck)[0]
    dealer_status[2] = deal_cards(deck)[1]
    print("\nThe dealer's hand is:", dealer_status[2][0],"[X]")

    # We check if the player holds a couple of A's (only hand of 2 cards higher than 21)
    player_ace_as_one = False
    player_status[1] = hand_sum(player_status[2], player_ace_as_one)

    if player_status[1] > 21:
        player_ace_as_one = True
        player_status[1] = hand_sum(player_status[2], player_ace_as_one)

    # We give the player the choice to take action
    player_status[3] = decide_player_action(player_status[2], player_status[1])

    while player_status[3] == "hit":

        player_status[2] = deal_one(player_status[2], deck)

        # Update player sum and status
        player_status[1] = hand_sum(player_status[2], player_ace_as_one)
        player_status = list(stl.settle_player(player_status, player_ace_as_one))

    # Dealer's play
    dealer_ace_as_one = False
    dealer_status[1] = hand_sum(dealer_status[2], dealer_ace_as_one)

    # Corner case: We check if the dealer holds a couple of A's (only hand of 2 cards higher than 21)
    if dealer_status[1] > 21:
        dealer_ace_as_one = True
        dealer_status[1] = hand_sum(dealer_status[2], dealer_ace_as_one)

    print("The dealer's hand is:", dealer_status[2])

    while (dealer_status[1] < 17) and (not player_status[0]):

        # Update hand and status
        dealer_status[2] = deal_one(dealer_status[2], deck)
        dealer_status[1] = hand_sum(dealer_status[2], dealer_ace_as_one)
        dealer_status = stl.settle_dealer(dealer_status)

    # We settle the game and update the pot
    pot = stl.settle_game(player_status, dealer_status, pot, bet)

    give_me_more = decide_keep_playing(pot)



