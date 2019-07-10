import sys

import dealing_of_cards as dc

deck_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4


# Game function

def game():
    """
    input: none
    external functions: deal_cards, hit, player, dealer
    takes both decks and defines who wins by comparing the sum of points according to the rules of Balckjack
    return: number of wins for player
    """

    wins = 0  # counter

    # call function for dealt cards
    player_hand = dc.deal_cards()
    dealer_hand = dc.deal_cards()

    print(f"You have {player_hand}")
    print(f"The dealer has {dealer_hand}")

    # call equivalent for point calculation of hand
    # change the name of ppoints and dpoint
    player_points = dc.player(player_hand)
    dealer_points = dc.dealer(dealer_hand)

    print(f"You have a total of {player_points}")
    print(f"The dealer has a total of {dealer_points}")

    return player_points, dealer_points

    # blackjack exception
    blackjack = False
    if player_points == 21:
        print("You win with blackjack!")
        wins += 1
        blackjack = True
    if player_points > 21:
        print("You lose, over 21")
        blackjack = True

    if dealer_points == 21:
        print("You lose, dealer has blackjack!")
        blackjack = True
    if dealer_points > 21:
        print("You win, dealer over 21")
        wins += 1
        blackjack = True

    # choice to hit or stand
    if not blackjack:
        choice = input("Do you want to hit or stand [h/s]?")

        # error handling
        if choice != "h" and choice != "s":
            print("Wrong input, make sure you enter only h or s [h/s], "
                  "you have one more chance or the game will end automatically.")
            choice = input("Do you want to hit or stand [h/s]?")
            if choice != "h" and choice != "s":
                print("Wrong input. ")
                sys.exit()

        # run hit
        elif choice == "h":
            print("hello")
            player_hand = dc.hit(player_hand)
            print(f"You now have {player_hand}")
            player_points = dc.player(player_hand)
            print(f"you have a total of {player_points}")
        if dealer_points < 17:
            dealer_hand = dc.hit(dealer_hand)
            print(f"The dealer now has {dealer_hand}")
            dealer_points = dc.dealer(dealer_hand)
            print(f"for a total of {dealer_points}")
        else:
            print(f"The dealer still has {dealer_hand}, for a total of {dealer_points}")

        # score resolution
        if player_points == 21:
            print("You win!")
            wins += 1
        elif dealer_points == 21:
            print("You lose!")
        elif player_points > 21:
            print("You lose!")
        elif dealer_points > 21:
            print("You win!")
            wins += 1
        elif player_points < dealer_points:
            print("You lose!")
        elif player_points > dealer_points:
            print("You win!")
            wins += 1
        else:
            print("You lose!")

    return wins
