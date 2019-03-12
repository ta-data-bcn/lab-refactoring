import functions as f
# importing functions library

finished, gen_number, lower_boundary, upper_boundary, tries, guess_range = f.initialization()
# Initialize the required variables and return the values, 'finished' is initially set to False


while not finished and tries != 0:
    # As long as the player does not guess the number right and tries have not run out
    # the following will keep executing

    guess_number = f.ask_guess(lower_boundary, upper_boundary)
    # Ask for input from player, comparing that number with the generated number,
    # and reset the boundary for each guess
    if guess_number == gen_number:  # Correct guess
        print(f"Congratulations! The number is {gen_number}. Game Over.")
        finished = True  # Exit while loop at the end of this iteration
    else:
        tries -= 1  # Tries minus one
        if tries == 0:  # Run out of guess
            print('YOU LOST!')
            finished = True  # Exit while loop at the end of this iteration
        else:
            lower_boundary, upper_boundary = f.determine_new_boundary(guess_number,lower_boundary,
                                                                      upper_boundary,gen_number)
            #  Reset new boundary with the new guess

    if finished:
        choice = input('Do you want to continue? (yes/no) ')
        #  When player either guess the number correctly or run out of guess, ask if he
        #  would like to start a new game, player input either yes or no

        if choice == 'yes':
            finished, gen_number, lower_boundary, upper_boundary, tries, guess_range = f.initialization()
            #  If yes is chosen, the game restart and all variables reset to values in f.initialization()
            #  for finished is reset to False, while-loop will execute



