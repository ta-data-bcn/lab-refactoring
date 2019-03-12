# Import turtle, a simple drawing library
import random
import turtle
from play import player_lost, player_won, turn

# List of english words and number of hangman pieces left variable
english_words = ['back', 'cheeks', 'chest', 'chin', 'ears', 'eyebrows', 'eyes', 'feet', 'fingers', 'foot', 'forehead',
                 'hair', 'hands', 'head', 'hips', 'knees', 'legs', 'lips', 'mouth', 'neck', 'nose', 'shoulders',
                 'teeth', 'stomach', 'teeth', 'throat', 'toes', 'tongue', 'tooth', 'waist'
                                                                                   'alligator', 'ant', 'bear', 'bee',
                 'bird', 'camel', 'cat', 'cheetah', 'chicken',
                 'chimpanzee', 'cow', 'crocodile', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'elephant', 'fish',
                 'fly', 'fox', 'frog', 'giraffe', 'goat', 'goldfish', 'hamster', 'hippopotamus', 'horse', 'kangaroo',
                 'kitten', 'lion', 'lobster', 'monkey', 'octopus', 'owl', 'panda', 'pig', 'puppy', 'rabbit', 'rat',
                 'scorpion', 'seal', 'shark', 'sheep', 'snail', 'snake', 'spider', 'squirrel',
                 'tiger', 'turtle', 'wolf', 'zebra']
n_pieces_left = 7

# Choose if the host is the machine or a human
machine_host_option = input('Choose who you want the \"Host\" to be. '
                            'If you want the word to be chosen by the machine type something and then press enter. '
                            'If you want a a human to chose the word, just press enter.')

if not machine_host_option:
    # Input host word variable
    host_word = input('Roses are red, Violets are blue... What are you!? Where are you!?\n'
                      'As the master player \"Host\" you will have the important task '
                      'of choosing the word that the players will have to guess! Now choose a word: ')

    # Checks if input is in alphabet and at least 1 letter for 100 times, if problem persists exit
    for i in range(100):
        if not host_word.isalpha() or len(host_word) == 0:
            host_word = input('Please remember to only one word. Not a number, not a phrase, just a word. Try again! ')
    if not host_word.isalpha() or len(host_word) == 0:
        exit()

    # Make input lower case
    host_word.lower()

else:
    host_word = random.choice(english_words)

# Correct guesses variable
correct_guesses = ['-'] * len(host_word)

# Easter eggs
if host_word in ['penguin', 'a human', 'a penguin', 'person', 'a person', 'human', 'barcelona',
                 'ironhack', 'ironhack campus', 'catalonia', 'spain', 'marina', 'earth', 'planet earth', 'the galaxy']:
    print('Congrats! You have found the hidden easter egg! You are awesome!')
    exit()

# Dictionary for pieces of hangman
hangman_parts = {7: 'upside down L', 6: 'head', 5: 'body', 4: 'arm', 3: 'arm', 2: 'leg', 1: 'leg'}

# Tell players how many letters the host_word has and new blank lines so the other players can't see the answer
for i in range(20):
    print('\n')
print('The host has chosen a word with ' + str(len(host_word)) + ' letters in it')

# Show screen and define "pen"
screen = turtle.Screen()
drawing_pen = turtle.RawPen(screen)
drawing_pen.hideturtle()

# For 100 times, if there isn't a clear winner or loser continue asking for letters and running turns
for i in range(100):
    if not player_won(correct_guesses) and not player_lost(n_pieces_left):
        guess = input('Please type the letter you think is in the hosts word: ')

        # Checks if input is in alphabet and only one character (one letter) for 100 times,
        # then exits program if user persists
        for ii in range(100):
            if not guess.isalpha() or len(guess) > 1 or len(guess) == 0:
                guess = input('Please remember to only type 1 letter. '
                              'Not a number, not a phrase, just a letter. Try again! ')
        if not guess.isalpha() or len(guess) > 1 or len(guess) == 0:
            print('Maximum times of tries reached. Exiting now.')
            exit()

        guess_l = guess.lower()

        # Run a turn with the guess and update correct_guesses and n_pieces_left
        correct_guesses, n_pieces_left = turn(guess_l, correct_guesses, n_pieces_left,
                                              hangman_parts, host_word, drawing_pen)
    else:
        break

# Print message depending if the player won or host won
if player_lost(n_pieces_left):
    a = input('Congrats you have lost! Losing is a part of learning so, don\'t worry, in a way you haven\'t lost. '
              'But not here, lol. Here you actually lost.')
else:
    print('Incredible! Amazing! Wonderful! Congrats, you actually won! Who would have said it...')
