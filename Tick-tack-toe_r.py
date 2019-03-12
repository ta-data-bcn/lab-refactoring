from beautifultable import BeautifulTable
from random import randint


def show_play(board):
    """
    It prints a table using the library BeautifulTable.
    The values are filled with the board argument.
    ------
    :param board:  3x3 list.
                3 dimensions list with 3 elements each.
    ------
    :return: Print a table as a board.
    """

    print("The game now is:")
    table = BeautifulTable()
    table.column_headers = ["", "1", "2", "3"]
    table.append_row(["x", board[0][0], board[0][1], board[0][2]])
    table.append_row(["y", board[1][0], board[1][1], board[1][2]])
    table.append_row(["z", board[2][0], board[2][1], board[2][2]])

    print(table)
    print("")


def machine_plays():
    """
    It returns the random values for the machine to play. A loop runs until an empty position is selected.
    ------
    :return: two int
    """

    print("Machine's turn!")
    ans_x_mach = randint(0, 2)
    ans_y_mach = randint(0, 2)

    while playboard[ans_y_mach][ans_x_mach] == "X" or playboard[ans_y_mach][ans_x_mach] == "O":
        ans_x_mach = randint(0, 2)
        ans_y_mach = randint(0, 2)

    return ans_y_mach, ans_x_mach


def transform(y):
    """
    Transform the values x, y or z by 0, 1 or 2, respectively.
    :param y:str that has to be x, y or z.
    :return: int: 0, 1 or 2
    """
    d_letter_to_num = {"x": 0, "y": 1, "z": 2}
    return d_letter_to_num[y]


def player_loop():
    """
    Ask the player which position wants to play.
    The programs keeps asking until the player select a correct spelled position.
    ------
    :return: two int
    """
    answer_x = input(
        "Your turn! Choose where you want to play. First, choose the horizontal coordinate: 1, 2 or 3: ")
    possible_x = ['1', '2', '3']
    while answer_x not in possible_x:
        answer_x = input("You didn't write a 1, 2 or 3. Please, choose the horizontal coordinate: 1, 2 or 3: ")
    answer_x = int(answer_x) - 1

    answer_y = input("And now the vertical coordinate: x, y or z: ")
    possible_y = ['x', 'y', 'z']
    while answer_y not in possible_y:
        answer_y = input("You didn't write a x, y or z. Please, choose the vertical coordinate: x, y or z: ")

    return transform(answer_y), answer_x


def player_plays():
    """
    Runs the player_loop function to get the player position. Then, check if the player has chosen an occupied position.
    If so, ask the player to select a new position.
    ------
    :return: two int
    """
    y, x = player_loop()

    while playboard[y][x] == "X" or playboard[y][x] == "O":
        print("You have chosen an occupied position! Please, repeat your play")
        y, x = player_loop()

    return y, x


def winning_cond():
    """
    It defines the winning conditions. There're two sections: machine and player.
    ------
    :return: True or False
    """

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
    """
    It returns true if the board is complete.

    :return: None or True
    """
    count = 0
    for i in playboard:
        for h in i:
            if h != "":
                count += 1
    if count == 9:
        print("Ohh, it's a draw... :(")
        return True
    else:
        return None


# Main section of the game, where the functions are called.

print("Welcome to Tick-tack-toe 3x3 game! You vs the drunk machine will be an amazing match!. "
      "Machine takes X and human O. Good luck!")

playboard = [["", "X", "O"],
             ["X", "O", "O"],
             ["", "X", ""]]

print("The initial board is:")

show_play(playboard)

print("The machine starts playing!")


while True:
    # The loop keeps the game running until a winning condition is fulfilled or is a draw.

    y_mac, x_mac = machine_plays()
    playboard[y_mac][x_mac] = "X"
    show_play(playboard)
    if winning_cond() is True:
        break
    if draw_game() is True:
        break

    y_hum, x_hum = player_plays()
    playboard[y_hum][x_hum] = "O"
    show_play(playboard)
    if winning_cond() is True:
        break
    if draw_game() is True:
        break

