from draw import draw_hangman_piece


# Function that outputs True if the player has lost
def player_lost(n_pieces_left):
    if n_pieces_left > 0:
        return False
    else:
        return True


# Function that outputs True if the player has won
def player_won(correct_guesses):
    return '-' not in correct_guesses


# Function that processes a turn
# and returns a different number of hangman parts and correct_guesses changes
# if one of them has to be changed
def turn(guess_, correct_guesses_, n_pieces_left_, hangman_parts, host_word, drawing_pen):
    # Copy of correct_guesses_list to do updates
    correct_guesses_out = correct_guesses_

    if guess_ in correct_guesses_:
        # If letter has already been guessed
        # ask for a new letter 100 times. If problem persists exit
        for it in range(100):
            guess_ = input('This letter has already been guessed! Please type a new one :) ')
            if guess_ not in correct_guesses_:
                break
        if guess_ in correct_guesses_:
            print('Maximum times of tries reached. Exiting now.')
            exit()

    if guess_ in host_word:
        # If letter hasn't been guessed and is correct
        # save it in the correct index of correct_guesses
        print('Correct! ' + guess_ + ' has been found')
        for index, char in enumerate(host_word):
            if char == guess_:
                correct_guesses_out[index] = guess_  # Update correct_guesses_out
        # Print correct guesses list for player context
        print(correct_guesses_out)

        return correct_guesses_out, n_pieces_left_
    else:
        # If letter hasn't been guessed and is incorrect
        # draw the corresponding hangman piece and subtract one to n_pieces_left
        print('Wrong letter... The host draw a: ' + hangman_parts[n_pieces_left_])
        draw_hangman_piece(n_pieces_left_, drawing_pen)

        return correct_guesses_, n_pieces_left_ - 1  # Update correct n_pieces_left
