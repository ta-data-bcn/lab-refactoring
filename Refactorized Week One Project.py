# The random function will select the word from our list of letters.
import random

def game():
    # Asks for players name, stores as name variable.
    name = input('What is your name?')

    # Takes name variable as input and returns as a string.
    def greet(name):
        print("Hello, " + name + ". Welcome to Hangman!")

    # This establishes wherever the player is familiar with the game or not and details rules if they're unfamiliar.
    # This is based on a user input prompt.

    def rules():
        # Basic function to ask wherever the player is familiar with the rules of the game.

        rules = input("Do you understand the rules of Hangman? Type N if you don't understand, Y to start playing!: ")

        # Ensure's that the player input works irregardless of wherever it is a capital or not.
        rules = rules.lower()

        # If they're familiar with the rule, the game carries on.
        if rules == 'y':
            print("Great, lets start the game! Have fun")
            return

        # If the player is not familiar, they're shown the rules, then asked for an input to continue.
        elif rules == 'n':
            print("""Hangman Rules - 
            You, the player, are given a random word which you need to guess. \n
            You must guess the word, one letter at a time. If you guess correctly, you win!\n
            There are a fixed number of guesses, so pick wisely!\n
            If exceed the maximum number of guesses you lose!\n
            Have fun!\n""")

        # This is an check to see if the player is inputting the correct response.
        elif rules != 'y' or rules != 'n':
            print("Please press Y or N!")
            return

    # Extracting the words from a text file of words obtained from GitHub.
    extract_words = open(
        "/Users/garethhughes/Desktop/Ironhack/Week_One/Project-Week-1-Build-Your-Own-Game/your-project/"
        "Dictionary/words.txt", 'r')

    # This first reads 'extract_words' which converts it into a string, which is then split by \n, then converted to a list
    extract_words = extract_words.read().split('\n')

    # Using the random module, we then randomly pick a word from the list of words.
    random_word = random.choice(extract_words)
    random_word_list = list(random_word)

    # This defines the game logic. The game is executed here.
    def gamelogic():

        # This states how long the random word selected is, gives the player
        # how many attempts that the player has based on the length of the word.
        # this means adjusts relative to the word.

        print("Your word is ", len(random_word), " long")
        attempts = int(len(random_word) + 3)
        print("You get", attempts, " attempts")

        # This keeps track of the number of correct letters guessed.
        # This value is updated as the player guesses correctly.

        correct_letters = 0

        # This places the whole game script into a while loop whereby
        # as long as the number of attempts are above zero, the code executes

        while attempts > 0:

            letter_check(player_letter, random_word)

            # The player can pick a letter. The loop also ensures that the player
            # only uses actual letters (not symbols / numbers) and only allows for
            # one letter at a time.

            player_letter = input('Pick a letter!: ')

            if player_letter.isalpha() == False:
                print('Please only enter letters')
            elif player_letter == 'hint':
                print(random_word[0:2])
            elif len(player_letter) > 1:
                print('Please enter only one letter')

            # This checks if the letter that the player chose is in the random word
            # If the letter IS in the random word, it increases the correct_letter variable by 1

            def letter_check(player_letter, random_word):
                if player_letter in random_word:
                    print('You guessed correctly!')
                    correct_letters += 1
                    return correct_letters
            print(correct_letters)

            # This is the win condition, whereby if the number of correct letters is equal to the
            # length of the random word. The program then stops.

            if correct_letters == len(random_word):
                print("You win! The word was", random_word)
                break

            # This is the incorrect word condition, if the letter isn't in the random word,
            # then 1 is substracted from the attempts amount.

            else:
                if player_letter not in random_word:
                    print('You guessed incorrectly')
                    attempts -= 1



        # once the attempts amount reaches zero, assuming that the win condition isn't reached first,
        # then the player loses and the hangman ASCII is displayed!

        if attempts == 0:
            print('You lose! The word was:', random_word)
            print('''
                        +---+
                          |   |
                          O   |
                         /|\  |
                         / \  |
                              |
                        =========''')

    greet(name)
    rules()
    gamelogic()