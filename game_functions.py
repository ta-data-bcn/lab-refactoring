import random


def initial_cash():

    cash = input("How much cash do you want to put into the table? (minimum cash-in is 50€, maximum 500€): ")

    while cash.isnumeric() == False or int(cash) > 500 or int(cash) < 50:
        cash = input("Allowed cash-in is between 50€ and 500€ ")

    return cash


def hand_bet(cash_remaining):

    bet = input("How much cash do you want to spend in the next round? (minimum bet is 50€, maximum 500€): ")

    while bet.isnumeric() == False or int(bet) > cash_remaining or int(bet) < 50:
        bet = input("Allowed bet is between 50€ and the cash you have remaining on the table: ")

    return bet


def dealing_cards(deck):

    hand_cards = [random.choice(list(deck.keys())), random.choice(list(deck.keys()))]
    return hand_cards


def value_cards_player(deck, player_cards):

    if "A" not in player_cards:
        hand = [deck[player_cards[0]],deck[player_cards[1]]]
        return sum(hand)

    elif player_cards[0] == "A" and player_cards[1] == "A":
        ace_value = input("Do you want your first ace to have a value of 1 or 11?: ")

        while ace_value not in ["1", "11"]:
            ace_value = input("Please indicate your ace's chosen value by typing 1 or 11 ")

        ace_value_2 = input("Do you want your second ace to have a value of 1 or 11?: ")

        while ace_value_2 not in ["1", "11"]:
            ace_value_2 = input("Please indicate your ace's chosen value by typing 1 or 11 ")

        hand = [int(ace_value), int(ace_value_2)]
        return sum(hand)

    else:

        ace_value = input("Do you want your ace to have a value of 1 or 11?: ")

        while ace_value not in ["1", "11"]:
            ace_value = input("Please indicate your ace's chosen value by typing 1 or 11 ")

        if player_cards.index("A") == 0:
            hand = [int(ace_value),deck[player_cards[1]]]
            return sum(hand)

        elif player_cards.index("A") == 1:
            hand = [deck[player_cards[0]], int(ace_value)]
            return sum(hand)


def value_cards_dealer(deck, dealer_cards):

    if "A" not in dealer_cards:
        dealer_hand = [deck[dealer_cards[0]],deck[dealer_cards[1]]]

    elif dealer_cards.index("A") == 0 and dealer_cards.index("A") == 1:
        dealer_hand = [deck[dealer_cards[0]][0],deck[dealer_cards[1]][1]]

    elif dealer_cards.index("A") == 0:
        dealer_hand = [deck[dealer_cards[0]][1], deck[dealer_cards[1]]]

    elif dealer_cards.index("A") == 1:
        dealer_hand = [deck[dealer_cards[1]][1], deck[dealer_cards[0]]]

    return sum(dealer_hand)


def checking_blackjack_preflop(bet, cash_remaining, player_hand_value, dealer_hand_value):

    if dealer_hand_value == 21:
        print("Dealer wins! - Blackjack")

        if cash_remaining == bet*(1.5):
            cash_remaining -= int(bet)

        else:
            cash_remaining -= int(bet)*(1.5)

        print("Your cash remaining is: %d €" % cash_remaining)
        return cash_remaining

    elif player_hand_value == 21:
        print("Player wins! - Blackjack")
        cash_remaining = cash_remaining + int(bet)*1.5
        print("Your cash remaining is: %d €" % cash_remaining)
        return cash_remaining

    else:
        return None


def keep_gambling(cash_remaining):

    question = input("Do you want to keep playing? (Y/N): ").upper()

    while question not in ["Y", "N"]:
        question = input("Please indicate whether you want to keep playing or leave by typing Y or N ").upper()

    if question == "N":
        print("Bye player. Your final cash is %d" % cash_remaining)

    else:
        print("\nOK, there we go")

    return question


def another_card():

    answer = input("\nDo you want another card? (Y/N): ").upper()

    while answer not in ["Y", "N"]:
        answer = input("Please indicate whether you want to fold or keep playing by typing Y or N ")

    return answer


def cards_post_flop(agent, deck_postflop, agent_cards, agent_hand_value):

    card_value = deck_postflop[random.choice(list(deck_postflop.keys()))]
    agent_cards.append(card_value)
    agent_hand_value += card_value
    print(f"\n{agent}'s card is {agent_cards[-1]}")
    print(f"{agent}'s hand value is {agent_hand_value}")
    return agent_cards, agent_hand_value


def busted(player_hand_value, dealer_hand_value, bet, cash_remaining):

    if player_hand_value > 21:
        print(f"Busted, Dealer wins!: ---> {dealer_hand_value}")
        cash_remaining = cash_remaining - int(bet)
        print("Your cash remaining is: %d €" % cash_remaining)
        return cash_remaining

    elif dealer_hand_value > 21:
        print(f"Busted, Player wins!")
        cash_remaining += int(bet)
        return cash_remaining


def final_results(player_hand_value, dealer_hand_value, bet, cash_remaining):

    if player_hand_value > dealer_hand_value:
        print("Player wins!")
        cash_remaining += int(bet)
        return cash_remaining

    elif player_hand_value < dealer_hand_value:
        print("Dealer wins!")
        cash_remaining -= int(bet)
        return cash_remaining

    elif player_hand_value == dealer_hand_value:
        print("This is a tie")
        cash_remaining = cash_remaining
        return cash_remaining


