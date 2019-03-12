# --- HANGMAN GAME --- #

# --- Import game modules  --- #

from drawing import draw_hangman
from words import choose_word

# --- Game functions --- #


def display_word():
    '''Word filled with underscores '_' if the letter has not been guessed yet, else shows the letter.
    :return: str'''
    print('\nUsed letters: ', used_letters)
    printed_word = ''
    for char in word:
        if char in guessed_letters:
            printed_word += char + ' '
        else:
            printed_word += '_ '
    return printed_word


def calc_max_mistakes():
    '''Calculates maximum number of mistakes depending on the length of the word.'''
    global max_mistakes
    if len(word) < 6:
        max_mistakes = 5
    elif 6 <= len(word) < 9:
        max_mistakes = 7
    else:
        max_mistakes = 9


def play():
    '''Main function to play the game.
    Calculates maximum number of mistakes with calc_max_mistakes().
    Iterates over a range which is the double of the word length.
    Asks user input, prints word with display_word() and draws hangman.
    Exits the game if an invalid input is passed.
    '''
    global mistakes
    calc_max_mistakes()
    for chance in range(len(word)*2):
        if mistakes == max_mistakes:
            break
        if not word_letters:
            print('Congratulations, you guessed the word!')
            break
        print(display_word())
        guess = input('\nPlease choose a letter: \n')
        if not guess.isalpha():
            return 'You have to enter a valid letter!!!'
        if guess in word_letters:
            word_letters.remove(guess)
            used_letters.append(guess)
            guessed_letters.append(guess)
        else:
            used_letters.append(guess)
            mistakes += 1
        draw_hangman(max_mistakes, mistakes)
    if word_letters:
        print(f'Game over! The word was {word}')


# --- Game initialization --- #

# Choose word
word = choose_word()

# Create empty set of the letters of chosen word
word_letters = set(word)

# Create empty lists in order to append the used letters and guessed letters after.
used_letters = []
guessed_letters = []

# Initialize mistakes and max_mistakes variables
mistakes = 0
max_mistakes = 0

# Call main function of the game
play()
