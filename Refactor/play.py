"""
# This library is in charge of the play flow. It will call the cards library to help with everything card related.

"""

import cards
import sys


def play():
    # First, we ask the player how much does he want to bet.
    bet = cards.place_bet()
    double_down = False

    # Check if he introduced a valid value.
    if bet is None:
        print("Program ending")

    # If he did, we proceed with the game
    else:
        # Deal the first 2 cards to dealer and player.
        player_hand = cards.deal_first_hand()
        print("Player's hand:", player_hand)
        dealer_hand = cards.deal_first_hand()
        print("Dealer's hand:", dealer_hand[0])

        # Check if any of them have a 21 with the first 2 cards.
        if cards.natural_blackjack(player_hand):
            print("Player wins with a natural blackjack!", player_hand)

        elif cards.natural_blackjack(dealer_hand):
            print("Dealer wins with a natural blackjack!", dealer_hand)

        # Check if the first 2 player's cards sum 9, 10, 11.
        else:
            if cards.check_double_down(player_hand):
                response = input("Would you like to double down? (Y/N):")

                if response == 'Y':
                    bet += bet
                    double_down = True
                    print("Your bet has doubled, now you're playing with: %d" % bet)

                elif response == 'N':
                    print("Your bet stays the same")

                else:
                    print("Invalid input, please introduce 'Y' or 'N' next time.")
                    sys.exit()

            # Set response to Y to enter the loop
            response = 'Y'
            while response == 'Y':
                # Check if player wants another card and if he can actually get one.
                response = input("Would you like another card? (Y/N): ")

                if response == 'Y' and cards.check_score(player_hand) <= 21:
                    cards.hit(player_hand)
                    print("Player's hand:", player_hand)
                    if double_down:
                        break
                    if cards.check_score(player_hand) > 21:
                        print("You bust with %d points. Dealer wins" % cards.check_score(player_hand))
                        sys.exit("Game over")
                    if cards.check_score(player_hand) == 21:
                        break

                elif response != 'Y' and response != 'N':
                    print("Invalid input, please introduce 'Y' or 'N' next time.")

            # After player is done with his hand, dealer plays.
            cards.dealer_play(dealer_hand)
            print("Player's hand: ", player_hand)

            # Both are done with their hands. Check scores and display result.
            cards.compare_hands(player_hand, dealer_hand, bet)
