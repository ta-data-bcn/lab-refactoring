# We need it for the computer's choice
import random

# A turn counter. Will get a +1 after every turn
turn_counter = 1

# A bool to check whose turn is it. Starts with True since human player always starts
player1_turn = False

# Global variables for players mark
player1_mark = None
player2_mark = None

# Dictionary to relate natural language positions to matrix positions
position_dict = {'top left': (0, 0), 'top': (0, 1), 'top right': (0, 2), 'left': (1, 0), 'center': (1, 1),
                 'right': (1, 2), 'bottom left': (2, 0), 'bottom': (2, 1), 'bottom right': (2, 2)}

# This initializing the board variable
board = None

# Only possible game board size for the current iteration of the software
board_size = 3

# The rules
rules = """This is Tic-Tac-Toe. You probably know it already.

In case you don't here are the rules:
- The game is played on a 3x3 board with empty spaces
- At the start of the game you choose either O or X as the symbol you want to use
- Each turn a player puts one of their symbol in an empty space
- A player wins when they manage to have 3 of their symbols
in any horizontal or vertical line or in one of the two long diagonals
- The game ends in a draw if there are no possible moves and the previous condition hasn't 
been met
- You can only play against the computer

When requesting a position to place a piece the program understands the following inputs: 'top left',
'top', 'top right', 'left', 'center', 'right', 'bottom left', 'bottom', 'bottom right'.

"""


# This prints the really ugly and nostalgic ASCII art logo
print("""

 _______  ___  _______       _______  _______  _______       _______  _______  _______ 
|       ||   ||       |     |       ||   _   ||       |     |       ||       ||       |
|_     _||   ||       | ____|_     _||  |_|  ||       | ____|_     _||   _   ||    ___|
  |   |  |   ||       ||____| |   |  |       ||       ||____| |   |  |  | |  ||   |___ 
  |   |  |   ||      _|       |   |  |       ||      _|       |   |  |  |_|  ||    ___|
  |   |  |   ||     |_        |   |  |   _   ||     |_        |   |  |       ||   |___ 
  |___|  |___||_______|       |___|  |__| |__||_______|       |___|  |_______||_______|

""")

# This is the first function that will be run, it resets all global to their default status in case it's a new game,
# including the board then runs function to let the player choose their mark, print the board and then runs
# check_turn() which takes over from here


def game_start():
    print(rules)
    global turn_counter
    turn_counter = 1
    global player1_mark
    player1_mark = None
    global player2_mark
    player2_mark = None
    global player1_turn
    player1_turn = False
    global board
    board = empty_board_generator()
    mark_choice()
    game_board_printer()
    check_turn()


# The name is self-explanatory
def empty_board_generator():
    return [[' ' for _ in range(3)] for _ in range(3)]


# This prints the game board, it will be called after each move
def game_board_printer():
    print(f"""{board[0][0]}|{board[0][1]}|{board[0][2]}
—————
{board[1][0]}|{board[1][1]}|{board[1][2]}
—————
{board[2][0]}|{board[2][1]}|{board[2][2]}

""")


# Lets the user choose the mark
def mark_choice():
    while True:
        # Constant variables during the game, that's why they're global
        global player1_mark
        global player2_mark

        user_input = input("""You will play against the computer since 
I haven't programmed 2-player games. Select O (as in Orange) or X (as in Xenobiology) 
as the symbol you want to play with:
        """).lower()

        if user_input == "x":
            print("""You chose X (as in Xenophobia). The computer will play with O 
(as in Organ trafficking).""")
            # First index is player1, second is player2
            player1_mark = "X"
            player2_mark = "O"
            break
        elif user_input == "o":
            print("""You chose O (as in Obamacare). The computer will play with X 
(as in  Xerox).""")
            # First index is player1, second is player2
            player1_mark = "O"
            player2_mark = "X"
            break
        else:
            print("""It's either X or O, I even gave you reference words, you can do this.""")
            continue


# This is what actually runs the game. The program goes back to this function after every turn,
# flips the player1_turn boolean and then either requests a choice from the player or the computer

def check_turn():
    global player1_turn
    global turn_counter
    if not player1_turn:
        # Switching True to False so that next turn it changes
        player1_turn = not player1_turn
        print(f"It's your turn and it's round number {turn_counter}.\n")
        turn_counter += 1
        request_position_from_user()
    else:
        player1_turn = not player1_turn
        print(f"It's the computer's turn and it's round number {turn_counter}.\n")
        turn_counter += 1
        computer_choice()


# This requests an input from the user
def request_position_from_user():
    position = input(f"Where do you want to put your {player1_mark.upper()}?").lower()
    check_for_empty_space(position)


def check_for_empty_space(position):
    if player1_turn:
        if position not in position_dict.keys():
            print("That is not an allowed position. Refer to the following list (DO NOT use apostrophes): 'top left',"
                  "'top', 'top right', 'left', 'center', 'right', 'bottom left', 'bottom', 'bottom right'.\n")
            request_position_from_user()
        elif position in position_dict.keys() and \
                board[position_dict[position][0]][position_dict[position][1]] != ' ':
            print("That position is already occupied, please choose a different one:\n")
            request_position_from_user()
        else:
            mark_placer(position)
    elif not player1_turn:
        # The computer will always choose from the position_dict, we just need to check if the space is occupied or not
        if position in position_dict.keys() and \
                board[position_dict[position][0]][position_dict[position][1]] != ' ':
            computer_choice()
        else:
            mark_placer(position)


# Random computer move
def computer_choice():
    check_for_empty_space(random.choice(list(position_dict.keys())))


# This places a mark at the given positions, prints a message to confirm the action, prints the board again
# and then runs the check_end_of_game function
def mark_placer(position):
    if player1_turn:
        board[position_dict[position][0]][position_dict[position][1]] = player1_mark
        print(f"You placed an {player1_mark} in the following position: {position}\n")
        game_board_printer()
        check_end_of_game()

    elif not player1_turn:
        board[position_dict[position][0]][position_dict[position][1]] = player2_mark
        print(f"The computer placed an {player2_mark} in the following position: {position}")
        game_board_printer()
        check_end_of_game()


# This checks when the game ends, either because someone won or because it's a tie
def check_end_of_game():
    global board_size
    # Checking horizontal lines
    for row in range(board_size):
        if all((mark == 'X') for mark in board[row]):
            end_of_game_announcer(board[row][0])
        elif all((mark == 'O') for mark in board[row]):
            end_of_game_announcer(board[row][0])
    # Zipping an unpacked nested list gives you the transposed list. Checking the horizontal lines in such a list
    # is the same as checking the verticals in the original one
    for column in zip(*board):
        if all((mark == 'X') for mark in column):
            end_of_game_announcer(column[0])
        elif all((mark == 'O') for mark in column):
            end_of_game_announcer(column[0])
    # Forward diagonal: both index are the same
    # It returns index 0,0 since there's just one diagonal, whereas there's 3 rows and 3 columns
    if all((mark == 'X') for mark in [board[i][i] for i in range(3)]):
        end_of_game_announcer(board[0][0])
    elif all((mark == 'O') for mark in [board[i][i] for i in range(3)]):
        end_of_game_announcer(board[0][0])
        # Inverse diagonal: The sum of the indexes of the points that are part of an inverse diagonal is equal to
        # board size -1
    elif all((mark == 'X') for mark in [board[i][board_size - i - 1] for i in range(3)]):
        end_of_game_announcer(board[0][2])
    elif all((mark == 'O') for mark in [board[i][board_size - i - 1] for i in range(3)]):
        end_of_game_announcer(board[0][2])
        # Checking if all squares are occupied
    elif all((mark == 'X' or mark == 'O') for mark in [mark for line in board for mark in line]):
        end_of_game_announcer("Tie")
    else:
        check_turn()


def end_of_game_announcer(mark):
    if mark == player1_mark:
        print("Congratulations, you won against a computer making random moves.")
    elif mark == player2_mark:
        print("You managed to let a computer choosing squares at random win a game of Tic-Tac-Toe.")
    elif mark == "Tie":
        print("It's a tie, there are no more spaces left. I guess you're as good as a random number generator.")
    while True:
        new_game = input("Would you like to play again? Y/N\n\n").lower()
        if new_game == "y":
            game_start()
        elif new_game == "n":
            raise SystemExit("Okay then, goodbye.")
        else:
            print("Please, input either Y or N.")


game_start()
