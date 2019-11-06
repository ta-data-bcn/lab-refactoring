''' The player has 3 different accions to do before reaching the final result, between hit(having another 
card), stay (the player is happy with his hand) or pass (the player does not want to play this round)'''


import opcions_game as og
import Change_A as ca



def accion(deck , money , bet , bet_in_table , hand_player , hand_dealer):
    accion = 0
    accion=int(input("\n Would you like to be Hit[1] again, you Stand[2] or you Pass[3]?  "))
    while accion !=1 and accion !=2 and accion !=3:
            print("\n Sorry, incorrect accion. You should put 1 (hit), 2(stand) or 3(pass)")
            accion=int(input("\n Would you like to be Hit[1] again, you Stand[2] or you Pass[3]?  "))
            
    if accion == 1:
        card= deck.pop()

        hand_player.append(card)

        hand_player = ca.change_A(hand_player,hand_dealer)[0]


        while sum(hand_dealer)<17:
            card= deck.pop()
            hand_dealer.append(card)
     
        money = og.opcions( money , bet , bet_in_table , hand_player , hand_dealer )

    elif accion == 2:
        while sum(hand_dealer)<17:
            card= deck.pop()
            hand_dealer.append(card)
             
        money = og.opcions(money, bet, bet_in_table, hand_player, hand_dealer)
        
        
    elif accion == 3:
        print(f"\n You pass the round. The dealer wins {bet_in_table}.")
        money -= bet 

    return money





