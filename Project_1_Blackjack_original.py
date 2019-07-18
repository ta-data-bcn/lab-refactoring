#!/usr/bin/env python
# coding: utf-8

# In[1]:
import random
import game_functions as gf


player_hand_value = 0
dealer_hand_value = 0


# In[2]:


gf.dealing_cards()

def value_cards_player():
 
    if "A" in player_cards:

        ace_value = input("By default your ace's value is 1, do you prefer it to be 11? (Y/N): ")

        while ace_value not in ["1", "11"]:
            ace_value = input("Please indicate your ace's chosen value by typing 1 or 11 ")

        if player_cards.index("A") == 0 and player_cards.index("A") == 1:
                hand = [int(ace_value), int(ace_value)]
                return sum(hand)

        elif player_cards.index("A") == 0:
                hand = [int(ace_value),deck[player_cards[1]]]
                return sum(hand)

        elif player_cards.index("A") == 1:       
                hand = [deck[player_cards[0]], int(ace_value)]
                return sum(hand)

    else:

        hand = [deck[player_cards[0]],deck[player_cards[1]]]
        return sum(hand)


def value_cards_dealer():
    if "A" not in dealer_cards:
        dealer_hand = [deck[dealer_cards[0]],deck[dealer_cards[1]]]
        
    elif dealer_cards.index("A") == 0 and dealer_cards.index("A") == 1:
        dealer_hand = [deck[dealer_cards[0]][0],deck[dealer_cards[1]][1]]
                       
    elif dealer_cards.index("A") == 0:
        dealer_hand = [deck[dealer_cards[0]][1], deck[dealer_cards[1]]]
                       
    elif dealer_cards.index("A") == 1:
        dealer_hand = [deck[dealer_cards[1]][1], deck[dealer_cards[0]]]

    return sum(dealer_hand)

def keep_gambling():
    question = input("Do you want to keep playing? (Y/N): ").upper()

    while question not in ["Y", "N"]:
        question = input("Please indicate whether you want to keep playing or leave by typing Y or N ")

    if cash_remaining < 50:
        question == "N"
    
    elif question == "N":
        print("Bye player. Your final cash is %d" % cash_remaining)
    
    else:
        print("\nOK, there we go")
        
    return question


# In[ ]:


question = "Y"

cash = input("How much cash do you want to put into the table? (minimum cash-in is 50€, maximum 500€): ")

while cash.isnumeric() == False or int(cash) > 500 or int(cash) < 50:
    cash = input("Allowed cash-in is between 50€ and 500€ ")

cash_remaining = int(cash)
    
while cash_remaining > 50 and question == "Y":
    
    bet = input("How much cash do you want to spend in the next round? (minimum bet is 50€, maximum 500€): ")

    while bet.isnumeric() == False or int(bet) > cash_remaining or int(bet) < 50:
        bet = input("Allowed bet is between 50€ and the cash you have remaining on the table")

    player_cards = gf.dealing_cards()
    dealer_cards = gf.dealing_cards()

    print(f"\nPlayer's initial hand is {player_cards}, and dealer's initial hand is {dealer_cards}")
    
    player_hand_value = value_cards_player()
    dealer_hand_value = value_cards_dealer()
    
    
    print(f"Player's initial hand value is {player_hand_value}, and dealer's initial hand value is {dealer_hand_value}")

    if dealer_hand_value == 21:
        print("Dealer wins! - Blackjack")
        cash_remaining = cash_remaining - int(bet)
        print("Your cash remaining is: %d €" % cash_remaining)
        question = keep_gambling()

    elif player_hand_value == 21:
        print("Player wins! - Blackjack")
        cash_remaining = cash_remaining + int(bet)*1.5
        print("Your cash remaining is: %d €" % cash_remaining)
        question = keep_gambling()

    else:

        while player_hand_value < 21:

            answer = input("\nDo you want another card? (Y/N): ").upper()

            while answer not in ["Y", "N"]:
                answer = input("Please indicate whether you want to fold or keep playing by typing Y or N ")

            if answer == "Y":
                cards = deck_postflop[random.choice(list(deck_postflop.keys()))]
                player_cards.append(cards)
                player_hand_value = player_hand_value + cards
                print(f"\nPlayer's card is {player_cards[-1]}")
                print(f"Player's hand value is {player_hand_value}")      

            elif answer == "N":
                break


        if player_hand_value > 21:
            print(f"Busted, Dealer wins!: ---> {dealer_hand_value}")
            cash_remaining = cash_remaining - int(bet)
            print("Your cash remaining is: %d €" % cash_remaining)
            question = keep_gambling()

        else:
            while dealer_hand_value < 17 or dealer_hand_value < player_hand_value:

                cards = deck_postflop[random.choice(list(deck_postflop.keys()))]
                dealer_cards.append(cards)
                dealer_hand_value = dealer_hand_value + cards
                print(f"Dealer's card is: {dealer_cards[-1]}")
                print(f"\nDealer's value hand is {dealer_hand_value}")

            if dealer_hand_value > 21:
                print(f"Busted, Player wins!")
                cash_remaining += int(bet)
                print(f"\nDealer's final hand is {dealer_hand_value}")

            else:

                if player_hand_value > dealer_hand_value:
                    print("Player wins!")
                    cash_remaining += int(bet)  
                elif player_hand_value < dealer_hand_value:
                    print("Dealer wins!")
                    cash_remaining -= int(bet)
                elif player_hand_value == dealer_hand_value:
                    print("This is a tie")
                    cash_remaining = cash_remaining
                
            print("Your cash remaining is: %d €" % cash_remaining)
            question = keep_gambling()

if cash_remaining < 50:
    print("You ran out of cash")


# In[ ]:




