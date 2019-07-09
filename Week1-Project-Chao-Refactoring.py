#!/usr/bin/env python
# coding: utf-8

# # Guess A Number Round 1

# ## This is a very simple game, you have to guess a number between 1 to 10. 
# ### You only have 3 chance.

# ------



import random



# Define the range of number we want to guess
range_min = 1
range_max = 10



# Define a max times one can guess
max_guess_time = 3




# Let the PC randomly create a number between 1-10 for guess
def pc_define_number():
    """
    To automatically generate a number between the maximum and minimum number we gave
    """
    number_to_guess = random.randint(range_min, range_max)
    return number_to_guess




# Now it's our time to guess a number. Input a number we guess
def give_a_guess():
    while True:  # This is to make the loop come back if the input is not a integer
        number_I_guess = input("Please guess a number between {} and {}: " .format(range_min, range_max))
        if number_I_guess.isnumeric():
            if (int(number_I_guess) >= range_min and int(number_I_guess) <= range_max):
                return number_I_guess
            else: 
                print("You can only choose a integer number between {} and {}".format(range_min, range_max))
        else:
            print("This is not a number! Please only input a number between {} and {}".format(range_min, range_max))




def guess_a_number():
    count = 0
    bingo = 0
    result = pc_define_number()  
    while (count < max_guess_time) and (bingo == 0):
        guess = int(give_a_guess())
        if result == guess:
            bingo += 1        
        elif result < guess:
            count += 1
            if count < max_guess_time:
                print("Maybe a bit lower?")
        else:
            count += 1
            if count < max_guess_time:
                print("hahaha, I am bigger than your guess~") 

    if bingo == 1:
        print("Bingo!! You should buy a lottery!")
    else:
        print("You didn't guess the number, the correct answer is {}".format(result))



#print("Welcome to the 'Guess A Number' game! You need to guess a number between {} and {} in three times".format(Range_min, Range_max))

guess_a_number()



# # Guess A Number Round 2

# ## Similar to the first game, now the range of number is biggher, but I will give you a hint. 
# ### Remember, you only have 5 chances.



# Define the range of number we want to guess
range_min = 1
range_max = 50




# Define a max times one can guess
max_guess_time = 5




# Let the PC randomly create a number between Range_min and Range_max for guess
def pc_define_number_with_hints():
    """
    The automatically generated number comes with a hint    
    """
    number_to_guess = random.randint(range_min, range_max)
    residue_by_3 = number_to_guess % 3
    residue_by_7 = number_to_guess % 7
    if (residue_by_3 == 0) and (residue_by_7 == 0):
        print("Hint: This number can be devided by 3 and 7")
    elif (residue_by_3 == 0) and (residue_by_7 != 0):
        print("Hint: This number can be devided by 3 but not by 7. If you devide this number by 7, the residue is {}" .format(number_to_guess % 7))        
    elif (residue_by_3 != 0) and (residue_by_7 == 0):
        print("Hint: This number can be devided by 7 but not by 3. If you devide this number by 3, the residue is {}" .format(number_to_guess % 3))
    else:
        print("Hint: This number can not be devided by 3 or 7")
    return number_to_guess
    



# Now it's our time to guess a number. Input a number we guess
def give_a_guess():
    while True:  # This is to make the loop come back if the input is not a integer
        number_I_guess = input("Please guess a number between {} and {}: " .format(range_min, range_max))
        if number_I_guess.isnumeric():
            if (int(number_I_guess) >= range_min and int(number_I_guess) <= range_max):
                return number_I_guess
            else: 
                print("You can only choose a integer number between {} and {}".format(range_min, range_max))
        else:
            print("This is not a number! Please only input a number between {} and {}".format(range_min, range_max))




def guess_a_number():
    count = 0
    bingo = 0
    result =  pc_define_number_with_hints()
    while (count < max_guess_time) and (bingo == 0):
        guess = int(give_a_guess())
        if result == guess:
            bingo += 1        
        elif result < guess:
            count += 1
            if count < max_guess_time:
                print("Maybe a bit lower?")
        else:
            count += 1
            if count < max_guess_time:
                print("hahaha, I am bigger than your guess~") 
    if bingo == 1:
        print("Bingo!! Did you get a 10/10 of math note in the high school?")
    else:
        print("Sorry, you didn't guess the number. The correct answer is {}".format(result))



guess_a_number()



# ---

# # Guess a Number Round 3

# ------

# ## Now, you need to guess a 4 digital number from 1000 to 9999. 
# ## The computer will tell you how many match (A) and mis-place (B) you have. 
# ### You have only 6 chances to guess the right number.



# Define the range of number we want to guess
range_min = 1000
range_max = 9999




# Define a max times one can guess
max_guess_time = 6



# Let the PC randomly create a number between 1-10 for guess
def pc_define_number():
    number_to_guess = random.randint(range_min, range_max)
    return number_to_guess




# Now it's our time to guess a number. Input a number we guess
def give_a_guess():
    while True:  # This is to make the loop come back if the input is not a integer
        number_I_guess = input("Please guess a number between 1000 and 9999: ")
        if number_I_guess.isnumeric():
            if (int(number_I_guess) >= range_min and int(number_I_guess) <= range_max):
                return number_I_guess
            else: 
                print("You can only choose a integer number between {} and {}".format(range_min, range_max))
        else:
            print("This is not a number! Please only input a number between {} and {}".format(range_min, range_max))




def guess_a_number2():
    count = 0
    bingo = 0
    result = str(pc_define_number())
    result2 = result
    while (count < max_guess_time) and (bingo == 0):
        correct = 0
        wrong_position = 0
        guess = give_a_guess()
        if result == guess:
            bingo += 1
        else:
            result = result2
            for digital in range(len(result)):
                if result == guess:
                    bingo += 1
                    break
                elif result[digital] == guess[digital]:
                    correct += 1
                    result = result.replace(result[digital], " ", 1)
                    guess = guess.replace(guess[digital], " ", 1)

                elif (guess[digital] in result):
                    wrong_position += 1
                    result = result.replace(guess[digital]," ", 1)
                    guess = guess.replace(guess[digital], " ", 1)

                   
        count += 1
        if (count < max_guess_time) and (bingo == 0):
            print(f"Your guess contains {correct}A{wrong_position}b")

    if bingo == 1:
        print("Bingo!! Do you have an IQ of 180?")
    else:
        print("Sorry, you didn't guess the number. The correct answer is {}".format(result2))




guess_a_number2()

