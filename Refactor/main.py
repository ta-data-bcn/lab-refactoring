import sys
import cards

def play():
    bet = cards.place_bet()
    player_hand = []
    dealer_hand = [9, 'A']
    player_wins = False
    dealer_wins = False
    tie = False
    response = 'Y'
    double_down = False

    if bet == None:
        print("Program ending")
    else:
        player_hand = cards.deal_first_hand()
        print("Player's hand:", player_hand)
        # dealer_hand = deal_first_hand()
        print("Dealer's hand:", dealer_hand[0])

        if cards.natural_blackjack(player_hand):
            print("Player wins with a natural blackjack!", player_hand)

        elif cards.natural_blackjack(dealer_hand):
            print("Dealer wins with a natural blackjack!", dealer_hand)

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

            response = 'Y'
            while response == 'Y':
                response = input("Would you like another card? (Y/N): ")

                if response == 'Y' and cards.check_score(player_hand) <= 21:
                    cards.hit(player_hand)
                    print("Player's hand:", player_hand)
                    if double_down:
                        break
                    if cards.check_score(player_hand) > 21:
                        print("You bust with %d points. Dealer wins" % cards.check_score(player_hand))
                        break

                elif response != 'Y' and response != 'N':
                    print("Invalid input, please introduce 'Y' or 'N' next time.")

            cards.dealer_play(dealer_hand)
            print("Player's hand: ", player_hand)
            p_score = cards.check_score(player_hand)
            d_score = cards.check_score(dealer_hand)

            if p_score > 21:
                print("You bust with %d points. Dealer wins" % p_score)

            elif d_score > 21:
                print("Dealer busts with %d points. Players wins" % d_score)

            elif p_score == d_score:
                print("There has been a tie. Player points: %d and hand: %s. Dealer points: %d and hand: %s" % (
                    p_score, player_hand, d_score, dealer_hand))

            elif p_score > d_score:
                print("Player wins with %d points with the hand %s" % (p_score, player_hand))

            elif p_score < d_score:
                print("Dealer wins with %d points with the hand %s" % (d_score, dealer_hand))

play()



