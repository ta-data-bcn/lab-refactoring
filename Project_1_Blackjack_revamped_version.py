import game_functions as gf
import constants as c


player_hand_value = 0
dealer_hand_value = 0


question = "Y"

CASH = gf.initial_cash()

cash_remaining = int(CASH)

while cash_remaining >= 50 and question == "Y":

    bet = gf.hand_bet(cash_remaining)

    player_cards = gf.dealing_cards(c.deck)
    dealer_cards = gf.dealing_cards(c.deck)

    print(f"\nPlayer's initial hand is {player_cards}, and dealer's initial hand is {dealer_cards}")

    player_hand_value = gf.value_cards_player(c.deck, player_cards)
    dealer_hand_value = gf.value_cards_dealer(c.deck, dealer_cards)

    print(f"Player's initial hand value is {player_hand_value}, and dealer's initial hand value is {dealer_hand_value}")

    blackjack = gf.checking_blackjack_preflop(bet, cash_remaining, player_hand_value, dealer_hand_value)

    if blackjack:
        cash_remaining = blackjack
        question = gf.keep_gambling(cash_remaining)

    else:

        while player_hand_value < 21:

            answer = gf.another_card()

            if answer == "Y":

                player_cards, player_hand_value = gf.cards_post_flop(c.player, c.deck_postflop, player_cards, player_hand_value)

            elif answer == "N":
                break

        if player_hand_value > 21:
            cash_remaining = gf.busted(player_hand_value, dealer_hand_value, bet, cash_remaining)
            question = gf.keep_gambling(cash_remaining)

        else:
            while dealer_hand_value < 17 or dealer_hand_value < player_hand_value:

                dealer_cards, dealer_hand_value = gf.cards_post_flop(c.dealer, c.deck_postflop, dealer_cards, dealer_hand_value)

            if dealer_hand_value > 21:
                cash_remaining = gf.busted(player_hand_value, dealer_hand_value, bet, cash_remaining)

            else:
                cash_remaining = gf.final_results(player_hand_value, dealer_hand_value, bet, cash_remaining)

            print("Your cash remaining is: %d €" % cash_remaining)
            question = gf.keep_gambling(cash_remaining)

if cash_remaining < 50 and question == "Y":
    print("You ran out of cash")
