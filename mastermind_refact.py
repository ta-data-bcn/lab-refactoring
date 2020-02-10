import random

def get_rounds():
    '''
    A function that asks the user for a positive number as an input and checks it.
    Input: none
    Output: a positive integer
    '''
    rounds_ok = False
    while rounds_ok == False:
        try:
            rounds = int(input('¿How many rounds do you want to play? '))
            if rounds > 0:
                rounds_ok = True
            else:
                raise ValueError(rounds)
        except ValueError:
            print('That is not a valid number of rounds! ')
        except NameError:
            print('That is not a valid number of rounds! ')
    return rounds


def instructions():
    '''
    A function that gives the user initial instructions for the game.
    Input: none
    Output: a positive integer (the number of rounds)
    '''
    print('')
    print('WELCOME TO MASTERMIND!')
    print('')
    print('In order to win the game, you will need to guess the secret code!')
    print('It is a code formed by 4 digits. Each digit is in the range of 1 to 6 (both included)')
    print('For each correct digit in the correct position, you will get a (x) key')
    print('For each correct digit in the wrong position, you will get a (o) key')      
    print(input('Are you ready? (press any key to start) '))
    number_of_rounds = get_rounds()
    return number_of_rounds


def random_code(available_numbers = 6, code_length = 4):
    '''
    A function that generates a random number
    Input: available_numbers (optional) as the range of numbers to be considered per each position of the code, 
    code_length (optional) as the lenght of the code
    Output: a list of four string elements
    '''
    rand_code = [str(random.randint(1, available_numbers)) for i in range(code_length)]
    return rand_code

def check_code(code, available_numbers = 6, code_length = 4):
    '''
    A function that checks the code input
    Input: available_numbers (optional) as the range of numbers to be considered per each position of the code, 
    code_length (optional) as the lenght of the code
    Output: boolean (True or False)
    '''
    return code.isdigit() and len(code) == code_length and all([int(position) in range(1, (available_numbers + 1)) for position in code])
        

def ask_code(available_numbers = 6, code_length = 4):
    '''
    A function that requests the user to input a code
    Input: available_numbers (optional) as the range of numbers to be considered per each position of the code, 
    code_length (optional) as the lenght of the code
    Output: a list of four string elements
    '''
    user_choice = input('Choose your code (leave no spaces between the numbers): ')
    while not check_code(user_choice):
        print('That\'s not a valid option! Remember your code must have', code_length, 'elements and only include integer numbers from 1 to ', available_numbers)
        user_choice = input('Choose your code (leave no spaces between the numbers): ')
    chosen_code = [i for i in user_choice]
    return chosen_code 

def check_round (cpu_choice, user_choice):
    '''
    A function that compares two codes and provides a result according to mastermind rules
    Input: cpu_code as the random code generated, user_choice as the code input from the user
    Output: black_pegs as the number of black pegs that the user guess earned, white_pegs as the
    number of white pegs that the user guess earned 
    '''
    code = cpu_choice.copy()
    guess = user_choice.copy()
    black_pegs = 0
    white_pegs = 0
    for x, y in zip(code, guess): 
        if x == y:
            black_pegs += 1
            code[code.index(x)] = '*'
            guess[guess.index(y)] = '-'
    for x in guess:
        if x in code: 
                white_pegs += 1
                code[code.index(x)] = '*'
    return black_pegs, white_pegs

def play_round (cpu_choice):
    '''
    A function that controls the round pipeline
    Input: cpu_choice as the random code generated,
    Output:  user_choice as the code input from the user, round_results as a tuple with the number of black
    and white pegs awarded 
    '''
    print('')
    print('')
    user_choice = ask_code()
    round_results = check_round(cpu_choice, user_choice)
    print('') 
    return user_choice, round_results

def check_game (user_choice, round_results, total_rounds):
    '''
    A function that checks the round and game results
    Input: user_choice as the code input from the user, round_results as a tuple with the number of black
    and white pegs awarded, total_rounds as the number of rounds to play
    Output: boolean (True or False)  
    '''
    print('                      ROUND ', i + 1, ':           Your guess is ', user_choice, '     Your key is ', ('x' * round_results[0]), ('o' * round_results[1]))
    if round_results[0] == 4:
        print('')
        print('') 
        print('|||||||||||||||||||||||||||||||||||||||||||||||||   YOU WIN   |||||||||||||||||||||||||||||||||||||||||||||||||')
        print('') 
        return True
    elif i + 1 == total_rounds:
        print('')
        print('') 
        print('|||||||||||||||||||||||||||||||||||||||||||||||||   YOU LOSE   ||||||||||||||||||||||||||||||||||||||||||||||||')
        print('') 
        return False
    else:
        return False

if __name__ == '__main__':

    ## INIT GAME
    total_rounds = instructions()
    cpu_choice = random_code()
    print(cpu_choice)
    
    ## PLAY ROUNDS
    for i in range(total_rounds):
        user_choice, round_results = play_round (cpu_choice)
        end_game = check_game (user_choice, round_results, total_rounds)
        if end_game == True:
            break
       