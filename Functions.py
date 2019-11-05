# Functions

# right_int() = Asking the user to insert a number from a range from 1 to 15. If the output from the user 
# is not an integer from 1 to 15, it will ask the user to enter the right output until he/she finally does it.


def right_int():

    n_num = "Please, type a number from 1 to 15: "
    w_num = "The number must be an integer from 1 to 15. Please, try again."
    n_user = input(n_num)

    while not n_user.isdigit() or int(n_user) not in range(1, 16):
        n_user = input(w_num)

    return int(n_user)

# While the user has attempts left, let the user insert an integer to keep guessing. 
# If the output of the user is higher than the one the machine choosed, let him know. 
# If the user output in lower, let him know.


def play(intentos, machine_n):
    while intentos >= 0:
        n_user = right_int()
        print(n_user)
        if n_user > machine_n:
            print('The number is higher than the one the machine chose.')
            intentos -= 1
            print(f'You have {intentos + 1} attempts left.')

        elif n_user < machine_n:
            print('The number is lower than the one the machine chose.')
            intentos -= 1
            print(f'You have {intentos + 1} left.')

        elif n_user == machine_n:
            return True

# Check who won. If the machine won, print it; if the user won, print it.

def final(winner, machine_n):
    if winner:
        print("Congatulations, YOU WON!!")
    else:
        print(f"the number chosed by the machine was: {machine_n}. GAME OVER")
