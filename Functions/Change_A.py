
'''In this function, we choose the card if the player has an As in his hand and the dealer also. 
the value between 1 or 11, depending on the player and the dealer has to take 1 if the other card is higher than 6.'''



def change_A(hand_player,hand_dealer): 
    if 'A' in hand_player:
        print(f"\n You have  an As in your hand {hand_player}.")
        if hand_player[0]=='A':
            hand_player[0]=int(input("\n Do you want the As to be value as 1 or 11? Insert value 1 or 11:  "))
            while hand_player[0] not in [1,11]:
                hand_player[0]=int(input("\n Please choose between 1 or 11 "))
        elif hand_player[1]=='A':
            hand_player[1]=int(input("\n Do you want the As to be value as 1 or 11? Insert value 1 or 11:  "))
            while hand_player[1] not in [1,11]:
                hand_player[1]=int(input("\n Please choose between 1 or 11 "))     

        

    elif 'A' in hand_dealer:
        if hand_dealer[0]=='A':
            if hand_dealer[1] <= 6:
                hand_dealer[0]=11
            else:
                hand_dealer[0]=1
                
        elif hand_dealer[1]=='A':
            if hand_dealer[0]<=6:
                hand_dealer[1]=11
                
            else:
                hand_dealer[1]=1

    return hand_player , hand_dealer  




#print(hand_player)
#print(hand_dealer)