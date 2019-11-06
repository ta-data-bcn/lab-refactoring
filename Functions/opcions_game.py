'''Here is where the magic happens, the different final game opcions, if the 
player wins againts the dealer or the other side.'''




def opcions(money ,bet ,bet_in_table , hand_player, hand_dealer):

    
    print(f"\n You have in hand {hand_player} with a total of {sum(hand_player)}")
    
    print(f"\n The dealer has in hand {hand_dealer} with a total of {sum(hand_dealer)}")

    if sum(hand_dealer)==21:
        print(f"\n Sorry you lose {bet}. The dealer got a Blackjack")
        money -= bet
        
    elif sum(hand_player)==21:
        print(f"\n You win against the dealer with a Blackjack. You win {bet_in_table}")
        money += bet_in_table
        
    elif sum(hand_player)>21:
        print(f"\n Sorry Mate. You busted. You lose {bet}")
        money -= bet
        
    
    elif sum(hand_dealer)>21:
        print(f"\n The dealer busted, lucky you. You win {bet_in_table}")
        money += bet_in_table
        
    
    elif sum(hand_player)<sum(hand_dealer):
        print(f"\n The dealer has  a higher hand than you. He won this round. You lose {bet}")
        money -= bet
        
    
    elif sum(hand_player)>sum(hand_dealer):
        print(f"\n You have a higher hand than the dealer. You win {bet_in_table}.")
        money += bet_in_table
        
    
    else:
        print("\n There has been a tie. Nobody wins")
        
        
    return money    