
# function to introduce the number of players who will play
def number_players_introduction():
    while True:
        try:
            number_players = int(input("Introduce a number of players which will play: "))
        except ValueError:
            print('Invalid number of players.')
            continue
        else:
            print ('The selected number of players is ' + str(number_players))
            print ('\n')
            break
    return number_players

# function which taking the number of players, creates lists and dictionaries with scores, wallet, the future hands, etc.
def create_dicts_scores_wallets (num_players):
    player_list = []
    wallet = {}
    score = {}
    hand = {}
    message_new_player = 'Introduce the name for Player {}: '
    welcome_new_player = 'Hello {}, welcome to Blackjack!'
    money_new_player = '{}, please introduce now the amount of money that you will lose today: '
    for i in range(num_players):
        player_name = input(message_new_player.format(i+1))
        print(welcome_new_player.format(player_name))
        while True:
            try:
                player_money = int(input(money_new_player.format(player_name)))
            except ValueError:
                print('Invalid amount of money.')
                continue
            else:
                print ('Okay! So {}€ then!. Enjoy the game!'.format(player_money))
                print ('\n')
                break
        player_list.append(player_name)
        wallet[player_name] = player_money
        score[player_name] = 0
        hand[player_name] = []
    # for score and hand, we also need to include the Dealer
    score['Dealer'] = 0
    hand['Dealer'] = []
    return player_list,wallet,score,hand

# function to place bets for all players at the start of a round
def place_bets (players):
    player_bets = {}
    
    global wallet
    
    for player in players:
        while True:
            try:
                player_bet = int(input('{}, you have {}€ left in your wallet. Please introduce how much money you will bet this round: '.format(player, wallet[player])))
            except ValueError:
                print('Invalid amount of money.')
                continue
            else:
                if player_bet > wallet[player]:
                    print ('The bet surpasses your amount of money left.')
                    continue
                else:
                    print ("{}'s bet is {}.".format(player, player_bet))
                    print ('\n')
                    break
        player_bets[player] = player_bet
    return player_bets

# helpful function which returns true if a hand has an Ace in it (they are special because their value may vary)
def is_ace (hand):
    
    global deck_values
    
    for card in hand:
        if type(deck_values[card]) == tuple:
            return True
    return False


# Function which take the name of the player and its hand and returns the corresponding score of the hand.
# It is a little bit tricky because of the Ace possibility of two values.
# Therefore if there is an Ace in the hand, the score is updated using tuples of two numbers (the two possible scores)
# depending on the value assigned to the Ace.
def score_update (player, hand):
    
    global deck_values
    
    if is_ace(hand): #calling the previous defined function
        hand_value = (0,0)
        count = 0
        for card in hand:
            if type(deck_values[card]) == tuple:
                if count == 0:
                    hand_value = tuple(map(sum, zip(hand_value, deck_values[card])))
                    count += 1
                else:
                    hand_value = tuple(map(sum, zip(hand_value, (1,1))))
            else:
                hand_value = tuple(map(sum, zip(hand_value, (deck_values[card],deck_values[card]))))
        if hand_value[0] > 21:
            hand_value = hand_value[1]
    else:
        hand_value = 0
        for card in hand:
            hand_value += deck_values[card]
    return hand_value

# helpful function which tells if a player (or the Dealer) has Blackjack. 
# It uses the fact that to have it you need to have an Ace, and therefore the score is stored as a tuple.
def blackjack(player):
    
    global score
    
    if type(score[player]) == tuple:
        if score[player][0]==21:
            return True
        else:
            return False
    else:
        return False


# This function acts as the phase when Blackjacks are checked for all players and the Dealer
def check_blackjack_phase ():
    
    global wallet
    global hands
    global final_player_list
    global player_bets
    
    if blackjack('Dealer'): #calling the previous function
        print('The second card of the Dealer is {}'.format(hands['Dealer'][1]))
        print('The Dealer has Blackjack! Everyone loses unless another Blackjack is in place.')
        for player in final_player_list:
            if blackjack(player): #calling previous function
                print ("{} has also got a Blackjack! This is a push.".format(player))
            else:
                print ("{} loses {}€".format(player, player_bets[player]))
                wallet[player] -= player_bets[player]
        print ('\n')
    else:
        for player in final_player_list:
            if blackjack(player): #calling previous function
                print ("Winner winner Chicken Dinner! {} has a Blackjack!".format(player))
                print ("{} wins {}€".format(player, round(player_bets[player]*1.5)))
                wallet[player] += round(player_bets[player]*1.5)
                print ('\n')


                
# Function that acts as the initial phase where two cards are dealt to each player and the Dealer
def drawing_round ():   
    
    global score
    global hands
    
    print ('Cards are being dealt...')
    print ('\n')
    for n in range(2):
        for player in score:
            hands[player].append(deck.pop())
    for pl,hnd in hands.items():
        if pl == 'Dealer':
            print('The Dealer got the following first card: {}'.format(hnd[0]))
            print('\n')
            break
        print("{}'s got the following hand: {}".format(pl,hnd))
    for pl in score.keys():
        score[pl] = score_update(pl, hands[pl])

# Function that draws a new card of the deck and updates the score on the corresponding player in the dict "score"
def draw_card(player):
    
    global deck
    global hands
    global score
    
    new_card = deck.pop()
    hands[player].append(new_card)
    score[player] = score_update(player, hands[player])
    print ("{} draws {}".format(player,new_card))

    
# this function acts as the Player phase, when all players go in turns in order to get cards or stand.
def player_round():
    
    global final_player_list
    global score
    global hands
    global wallet
    global player_bets
    
    for player in final_player_list:
        if blackjack(player):
            print("{} has already a Blackjack, and does not take the turn.".format(player))
            print('\n')
            continue
        else:
            print ("It's {}'s turn!".format(player))
            print ('You have bet {}€'.format(player_bets[player]))
            while True:
                print ('Your hand is now {}'.format(hands[player]))
                if type(score[player])==tuple:
                    print ("{}'s hand value may be {} or {}.".format(player, score[player][0], score[player][1]))
                else:
                    print ("Your hand's value is {}".format(score[player]))
                hit_stand = input('Dou you want to Hit(draw a new card) or Stand(hold and end your turn)? Please use (h/s) ')
                while hit_stand not in ('h','s'):
                    hit_stand = input('Please introduce a valid command: Hit (h) or Stand (s): ') 
                if hit_stand == 'h':
                    draw_card(player)
                    if type(score[player])!= tuple :
                        if score[player] > 21:
                            print ("It's a burst! You surpassed 21. You lose {}€".format(player_bets[player]))
                            wallet[player] -= player_bets[player]
                            print ('\n')
                            break
                        elif score[player] == 21:
                            print ("You reached exactly 21. Congrats! You will win if the Dealer does not reach 21!")
                            print ('\n')
                            break
                    else:
                        if score[player][0] == 21:
                            score[player] = score[player][0]
                            print ("You reached exactly 21. Congrats! You will win if the Dealer does not reach 21!")
                            print ('\n')
                            break
                else:
                    if type(score[player])!=tuple:
                        print('You stand. Your final score is {}'.format(score[player]))
                        print ('\n')
                    else:
                        print('You stand. Your final score is {}'.format(score[player][0]))
                        print ('\n')
                        score[player] = score[player][0]
                    break

                    
# function that is similar to the player_round function but is automatized for the Dealer.
def dealer_round():
    
    global score
    global hands
    
    print("It's the turn of the Dealer.")
    print("Dealer's complete hand: {}".format(hands['Dealer']))
    if type(score['Dealer'])==tuple:
        print ("Dealer's hand value may be {} or {}.".format(score['Dealer'][0], score['Dealer'][1]))
    else:
        print ("Dealer's hand value is {}".format(score['Dealer']))
    while True:
        if type(score['Dealer'])==tuple:
            if score['Dealer'][0] > 16:
                score['Dealer'] = score['Dealer'][0]
                print ("Dealer stands")
                print ("Dealer's final hand is {}".format(hands['Dealer']))
                print ("Dealer's final score is {}".format(score['Dealer']))
                print ('\n')
                break
            else:
                draw_card('Dealer')
        else:
            if score['Dealer'] > 21:
                print ('The Dealer is busted! All remaining players win!')
                print ('\n')
                break
            elif score['Dealer'] > 16:
                print ("Dealer stands")
                print ("Dealer's final hand is {}".format(hands['Dealer']))
                print ("Dealer's final score is {}".format(score['Dealer']))
                print ('\n')
                break
            else:
                draw_card('Dealer')

                
# function that compares the final scores for all remaining players and updates wallets.
def final_score():
    
    global score
    global wallet
    global player_bets
    global final_player_list
    
    print ('This is the final score!')
    final_score = score.copy()
    for pl,sc in final_score.items():
        if blackjack(pl):
            sc = 'Blackjack!'
        elif sc > 21:
            sc = 'Bust!'
        print ("{}: {}".format(pl,sc))
    print ('\n')
    if not blackjack('Dealer'):
        if score['Dealer'] > 21:
            for player in final_player_list:
                if not blackjack(player):
                    if score[player] < 22:
                        print ("{} wins {}€".format(player, player_bets[player]))
                        wallet[player] += player_bets[player]
            print ('\n')
        else:
            for player in final_player_list:
                if not blackjack(player):
                    if score[player] < 22:
                        if score[player] < score['Dealer']:
                            print ("{} loses {}€".format(player, player_bets[player]))
                            wallet[player] -= player_bets[player]
                        elif score[player] > score['Dealer']:
                            print ("{} wins {}€".format(player, player_bets[player]))
                            wallet[player] += player_bets[player]
                        else:
                            print ("{} recovers the bet of {}€".format(player, player_bets[player]))
    print('\n')

    
# function that checks if a player has 0 money in wallet and eliminates him.
# Also resets the "player_bets", "score" and "hands" dictionaries.
# Finally asks if players want another round, if they do, a new round is played, if they don't, the final game triggers.
# The final game displays the remaining wallet for each player (including eliminated), as well as how much money they have won/lost.
# If no player has money left, end of game triggers automatically.
def end_of_round():
    
    global player_list
    global final_player_list
    global wallet
    global score
    global hands
    global player_bets
    global initial_wallet
    
    for player in player_list:
        if player not in final_player_list:
            print("{} has been eliminated".format(player))
        else:
            print("{}'s wallet has now {}€'".format(player,wallet[player]))
            if wallet[player] == 0:
                print("{} has no money left! {} is eliminated!".format(player,player))
                final_player_list.remove(player)
                del score[player]
                del hands[player]
                del player_bets[player]
    print('\n')
    print('\n')
    # Reset of all parameters just in case:
    for player in final_player_list:
        player_bets[player]=0
        score[player]=0
        hands[player]=[]
    score['Dealer']=0
    hands['Dealer']=[]
    if not final_player_list:
        play_again = 'n'
    else:
        play_again = input('Do you wanna play again? [y/n] ')
    while play_again not in ('y','n'):
        play_again = input('Please introduce a valid command: Yes(y) or No(n): ')
    if play_again == 'n':
        wannaplay = False
        print('\n')
        print ('Game Final Money:')
        for player in player_list:
            if player not in final_player_list:
                print("{}: 0€ (-{}€)".format(player,initial_wallet[player]))
            else:
                if wallet[player] >= initial_wallet[player]:
                    print("{}: {}€ (+{}€)".format(player,wallet[player],wallet[player]-initial_wallet[player]))
                else:
                    print("{}: {}€ (-{}€)".format(player,wallet[player],initial_wallet[player]-wallet[player]))
        print('\n')
        print('See all you in another game of Blackjack!')
    else:
        wannaplay = True
    return wannaplay
