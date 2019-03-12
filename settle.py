import deck_values as dv
import player_action as pa


def settle_player(player_sum, player_hand, player_ace_as_one):

    player_busted = False

    if player_sum > 21 and 'A' not in player_hand:
        print(player_hand, "\nYou are now at", player_sum, "\nBusted!")
        action = "pass"
        player_busted = True

    elif player_sum > 21 and 'A' in player_hand:
        player_ace_as_one = True
        player_sum = dv.hand_sum(player_hand, player_ace_as_one)

        if player_sum > 21:
            print(player_hand, "\nYou are now at", player_sum, "\nBusted!")
            action = "pass"
            player_busted = True
        else:
            action = pa.decide_player_action(player_hand, player_sum)

    elif player_ace_as_one:
        action = pa.decide_player_action(player_hand, player_sum)

    else:
        action = pa.decide_player_action(player_hand, player_sum)

    return player_busted, player_sum, action


