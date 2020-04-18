# A game of blackjack

# defining the deck
import random
deck = list(("2", "3", "4", "5", "6", "7", "8", "9", "10", "J" , "Q", "K", "A")*4)
random.shuffle(deck)
print(deck)
cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':1}

# Initial player cards
player = random.sample(deck,2)
for i in player:
    deck.remove(i)
    
# Initial dealer cards
dealer = random.sample(deck,2)
for i in dealer:
    deck.remove(i)
    
# Initial cards
player_sum = sum(map(cards.get, player))
dealer_sum = sum(map(cards.get, dealer))

# Asking the player, play and number of rounds
want_to_play = input("Would you like to play a round of Black Jack?")
n = []

while True:
    if want_to_play in ["y", "Y", "Yes", "yes", "YES", "YEAH", "yeah", "yeah!", "YEAH!", "alright", "Ok", "ok"]:
        rounds = input("How many rounds would you like to play?" )
        while sum(n) <= int(rounds):
            print("You have " , player)
            game()
            break
        else:
            print("Ok, byebye!")
            break

# Game as a function: defines the players coices, the hands and the outcomes
def game():
    global player
    global dealer
    global player_sum
    global dealer_sum
    global rounds
    global n
    while player_sum < 21:
        player_choice = input("Would you like to stay or hit? ")
        if player_choice in ["hit" , "Hit", "HIT", "h", "H"]:
            random_card_p = random.sample(deck,1)[0]
            player.append(random_card_p)
            deck.remove(random_card_p)
            player_sum = sum(map(cards.get, player))
            if dealer_sum < 17:
                random_card_d = random.sample(deck,1)[0]
                dealer.append(random_card_d)
                deck.remove(random_card_d)
                dealer_sum = sum(map(cards.get, dealer))
            print("You have " , player, "summing up to " , player_sum)
            if dealer_sum > 21:
                       print("You win with " , player, "the dealer busted!")
        else:
            player_result = 21 - player_sum
            dealer_result = 21 - dealer_sum
            if player_result < dealer_result:
                print("Huuurraayy! You win! You have " , player,"summing up to ",  player_sum)
                print("The dealer only had ", dealer, "summing up to ", dealer_sum)
                break
            if player_result > dealer_result:
                print("Uh ohh... you lose. You have " , player, "summing up to " ,player_sum)
                print("The dealer has ", dealer, "summing up to " , dealer_sum)
                break
            if player_result == dealer_result:
                print("Oh - it's a tie!")
                break
    if player_sum == 21:
        print("Huurray you have BLACK JACK! You win!")
    if dealer_sum == 21:
        print("Uhh ohh. You lose! The dealer had 21. hehehe")
    if player_sum > 21:
        print("Uhh ohh. You lose! You have more than 21. hehehe")
    if dealer_sum > 21:
        print("You win! The dealer has more than 21!")
    n.append(1)

# Asking the player, play and number of rounds
while True:
    if want_to_play in ["y", "Y", "Yes", "yes", "YES", "YEAH", "yeah", "yeah!", "YEAH!", "alright", "Ok", "ok"]:
        rounds = input("How many rounds would you like to play?" )
        while sum(n) <= int(rounds):
            print("You have " , player)
            game()
            break
        else:
            print("Ok, byebye!")
            break
