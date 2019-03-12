from beautifultable import BeautifulTable
import random


def show_play(board):
    # Here I print the board.

    print("The game now is:")
    table = BeautifulTable()
    table.column_headers = ["", "1", "2", "3"]
    table.append_row(["x", board[0][0], board[0][1], board[0][2]])
    table.append_row(["y", board[1][0], board[1][1], board[1][2]])
    table.append_row(["z", board[2][0], board[2][1], board[2][2]])

    print(table)
    print("")


def machine_plays():
    # Here I take random values for the machine to play. There's a loop until is chosen a non occupied position.

    print("Machine's turn!")
    ans_x_mach = random.randint(0, 2)
    ans_y_mach = random.randint(0, 2)

    while playboard[ans_y_mach][ans_x_mach] == "X" or playboard[ans_y_mach][ans_x_mach] == "O":
        ans_x_mach = random.randint(0, 2)
        ans_y_mach = random.randint(0, 2)

    return ans_y_mach, ans_x_mach


def player_plays():
    # Here I ask the player which position she/he wants to play.

    answer_x = input("Your turn! \n"
                    "Choose where you want to play. First, choose the horizontal coordinate: 1, 2 or 3: ")
    possible_a = ['1', '2', '3']
    while answer_x not in possible_a:
        answer_x = input("You didn't write a 1, 2 or 3. Please, choose the horizontal coordinate: 1, 2 or 3: ")

    answer_x = int(answer_x) - 1



    answer_y = input("And now the vertical coordinate: x, y or z: ")
    possible_b = ['x', 'y', 'z']
    while answer_y not in possible_b:
        answer_y = input("You didn't write a x, y or z. Please, choose the vertical coordinate: x, y or z: ")

    trans_y = ""
    if answer_y == "x":
        trans_y = 0
    elif answer_y == "y":
        trans_y = 1
    elif answer_y == "z":
        trans_y = 2

    while playboard[trans_y][answer_x] == "X" or playboard[trans_y][answer_x] == "O":

        answer_x = input("You have chosen an occupied position. Please, choose an empty one. First, choose the horizontal coordinate: 1, 2 or 3: ")
        possible_a = ['1', '2', '3']
        while answer_x not in possible_a:
            answer_x = input("You didn't write a 1, 2 or 3. Please, choose the horizontal coordinate: 1, 2 or 3: ")

        answer_x = int(answer_x) - 1

        answer_y = input("And now the vertical coordinate: x, y or z: ")
        possible_b = ['x', 'y', 'z']
        while answer_y not in possible_b:
            answer_y = input("You didn't write a x, y or z. Please, choose the vertical coordinate: x, y or z: ")

        trans_y = ""
        if answer_y == "x":
            trans_y = 0
        elif answer_y == "y":
            trans_y = 1
        elif answer_y == "z":
            trans_y = 2


    return trans_y, answer_x


def winning_cond():
    # Here I define the winning conditions

    # Machine wins

    if playboard[0][0] == playboard[0][1] == playboard[0][2] == "X":
        print("Drunk Machine wins! Congrats!")
        return True

    elif playboard[1][0] == playboard[1][1] == playboard[1][2] == "X":
        print("Drunk Machine wins! Congrats!")
        return True

    elif playboard[2][0] == playboard[2][1] == playboard[2][2] == "X":
        print("Drunk Machine wins! Congrats!")
        return True

    elif playboard[0][0] == playboard[1][0] == playboard[2][0] == "X":
        print("Drunk Machine wins! Congrats!")
        return True

    elif playboard[0][1] == playboard[1][1] == playboard[2][1] == "X":
        print("Drunk Machine wins! Congrats!")
        return True

    elif playboard[0][2] == playboard[1][2] == playboard[2][2] == "X":
        print("Drunk Machine wins! Congrats!")
        return True

    elif playboard[0][0] == playboard[1][1] == playboard[2][2] == "X":
        print("Drunk Machine wins! Congrats!")
        return True

    elif playboard[0][2] == playboard[1][1] == playboard[2][0] == "X":
        print("Drunk Machine wins! Congrats!")
        return True

    # Human wins

    if playboard[0][0] == playboard[0][1] == playboard[0][2] == "O":
        print("You wins! Congrats!")
        return True

    elif playboard[1][0] == playboard[1][1] == playboard[1][2] == "O":
        print("You wins! Congrats!")
        return True

    elif playboard[2][0] == playboard[2][1] == playboard[2][2] == "O":
        print("You wins! Congrats!")
        return True

    elif playboard[0][0] == playboard[1][0] == playboard[2][0] == "O":
        print("You wins! Congrats!")
        return True

    elif playboard[0][1] == playboard[1][1] == playboard[2][1] == "O":
        print("You wins! Congrats!")
        return True

    elif playboard[0][2] == playboard[1][2] == playboard[2][2] == "O":
        print("You wins! Congrats!")
        return True

    elif playboard[0][0] == playboard[1][1] == playboard[2][2] == "O":
        print("You wins! Congrats!")
        return True

    elif playboard[0][2] == playboard[1][1] == playboard[2][0] == "O":
        print("You wins! Congrats!")
        return True

    else:
        return False

def draw_game():
    count = 0
    for i in playboard:
        for h in i:
            if h != "":
                count += 1
    if count == 9:
        print("Ohh, it's a draw... :(")
        return True

# Here I define the start of the game.

print("Welcome to Tick-tack-toe 3x3 game! You vs the drunk machine will be an amazing match!. "
      "Machine takes X and human O. Good luck!")
zip()


playboard = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

print("The initial board is:")

show_play(playboard)

print("The machine starts playing!")


while True:
    #Here I create a loop that keeps the game running until a winning condition is fulfilled.

    ans_y_mac, ans_x_mac = machine_plays()

    playboard[ans_y_mac][ans_x_mac] = "X"

    show_play(playboard)

    if winning_cond() is True:

        break

    if draw_game() is True:

        break


    ans_y_hum, ans_x_hum = player_plays()

    playboard[ans_y_hum][ans_x_hum] = "O"

    show_play(playboard)

    if winning_cond() is True:

        break

    if draw_game() is True:

        break

