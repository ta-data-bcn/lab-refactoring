#prints drawing of hangman
import turtle
def hangman(attempts):
    if attempts == 1:
        turtle.penup()
        turtle.setposition(-200,-100)
        turtle.pendown()
        turtle.setheading(90)
        turtle.fd(400)

    elif attempts == 2:
        turtle.setheading(0)
        turtle.fd(300)

    elif attempts == 3:
        turtle.setheading(270)
        turtle.fd(70)

    elif attempts == 4:
        turtle.penup()
        turtle.setheading(180)
        turtle.fd(0)
        turtle.pendown()
        turtle.circle(30)
        turtle.penup()
        turtle.setheading(270)
        turtle.fd(60)
        turtle.pendown()

    elif attempts == 5:
        turtle.fd(100)

    elif attempts == 6:
        turtle.setheading(90)
        turtle.fd(50)
        turtle.setheading(0)
        turtle.fd(50)

    elif attempts == 7:
        turtle.back(100)

    elif attempts == 8:
        turtle.fd(50)
        turtle.setheading(270)
        turtle.fd(50)
        turtle.setheading(0)
        turtle.fd(50)

    else:
        turtle.back(100)

#Guess a letter: It gathers the guess (checking and formating to the correct format
def guessletter():
    while True:
        p_guess = input("Make your guess, tell me a letter: ")
        p_guess=p_guess.lower()

        if p_guess.isalpha():
            return p_guess

        else:
            print("Sorry I don't understand you, enter another letter :(")


#Confirmation of guessing the word
def guesswordconsent():
    while True:
        p_guess1=input("\nDo you want to try to guess the word? Y, N: ")

        if p_guess1.isalpha():

            if p_guess1.lower() in ["yes", "y", "si", "sí", "yas", "s"]:
                p_guess1="yes"
                return p_guess1

            elif p_guess1.lower() in ["no", "n", "nou"]:
                p_guess1="no"
                return p_guess1

            else:
                print("Sorry I don't understand your answer, you have to type Y or N: ")

        else:
            print("-------------Sorry I don't understand you, enter Y or N")


#Try to guess the word
def guessword():
    while True:
        p_guess=input("\nEnter your guess of the word: ")
        p_guess=p_guess.lower()

        if p_guess.isalpha():
            return p_guess

        else:
            print("Sorry I don't understand you, enter another letter")