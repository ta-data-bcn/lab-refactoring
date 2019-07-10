import random
import string
import time

# Generation of a personalized password by using two individual and personal words of the user


# Variables and lists needed to generate
    # Where FIRST_WORD & SECOND_WORD represent the global variables
users_actual_words = {"FIRST_WORD": "", "SECOND_WORD": ""}
user_words_modified = {"FIRST_WORD": "", "SECOND_WORD": ""}

leetspeak_dictionary = {"i": "!", "l":1, "z": 2, "e": 3, "a": 4, "s": 5, "g": 6, "t": 7, "b": 8, "g": 9, "o": 0 }

topic_list_1 = ["School", "Home", "Balcony", "Church", "Garden"]
topic_list_2 = ["Fruit", "Animal", "Sport", "Country", "Subject"]


# Functions used for the generation of the password

def questions_to_user():
    """
    # A function that asks the user for his input. Depending on whether the user has two individual words
      in mind ("yes" or "no") a different path to generate the password will be used.
      The personal words will be saved in global variables
    """
    users_path = (input("You have two words for your password in mind? (yes/no) :")).lower()

    # Until the user gives the right input, we will keep asking him the same question (with a punishment of 3 seconds
    # for answering if the the answer is not "yes" or "no"
    while users_path not in ["yes", "no"] :
        print("\n Oje, that was wrong. You should type " "\033[1m" "yes" "\033[0m" " or " "\033[1m" "no" "\033[0m")
        time.sleep(3)
        users_path = input("\n Again, do you have two suitable words for your password in mind? (yes/no) :")

    # If the users answer is "yes" (so he has two words in mind), the two words will be saved in the global variables
    # FIRST_WORD and SECOND_WORD
    if users_path == "yes":
        users_word_1 = input("\n In this case, please type in the first word that should be in your password :")
        users_actual_words["FIRST_WORD"] = users_word_1.upper()
        user_words_modified["FIRST_WORD"] = users_actual_words["FIRST_WORD"]

        users_word_2 = input("\n Perfect. Now, please type in the second word :")
        while len(users_word_2) + len(users_word_1) < 7:
                print( f"\n jajaja ... The aim is to create a strong password. Thus we need a longer word. Your first password has {len(users_word_1)} letters. So this word should have at least {7-len(users_word_1)} letters. Try another word")
                time.sleep(3)
                users_word_2 = input("Please type in your word:")
        users_actual_words["SECOND_WORD"] = users_word_2.upper()
        user_words_modified["SECOND_WORD"] = users_actual_words["SECOND_WORD"]

        time.sleep(1)
        return "\n ______CALCULATING______"

    # If the users answer is "no" (so he has NOT two words in mind), the user will choose for each word a topic from the
    # topic_lists to find two individuals words. These two will be saved in the global variables FIRST_WORD and SECOND_WORD
    elif users_path == "no":
        users_path_1 = input(f"Choose one of the following topics by tipping it in {topic_list_1} :")
        while users_path_1 not in topic_list_1:
            print("\n It is strongly recommended to pick a topic of the given list. Only this way" "\033[1m" " a strong password that is also rememberable " "\033[0m" "can be guaranteed")
            time.sleep(3)
            users_path_1 = input(f"Please choose one of the following topics by tipping it in {topic_list_1} :")
        users_word_1 = input(f"So the topic is {users_path_1}, perfect. Now, imagine that it is a sunny and warm day. Imagine how you step into your {users_path_1}. Please type in the first word that pops up your mind thinking about this :")
        users_actual_words["FIRST_WORD"] = users_word_1.upper()
        user_words_modified["FIRST_WORD"] = users_actual_words["FIRST_WORD"]

        users_path_2 = input(f"Que bien, we are almost there. Please choose one of the following topics by tipping it in {topic_list_2} :")
        while users_path_2 not in topic_list_2:
            print("\n It is strongly recommended to pick a topic of the given list. Only this way" "\033[1m" "a strong password that is also rememberable" "\033[0m" "can be guaranteed")
            time.sleep(3)
            users_path_2 = input(f"Please choose one of the following topics by tipping it in {topic_list_2} :")
        users_word_2 = input(f"The second word will be your favourite {users_path_2}. Please type it in :")
        while len(users_word_2) + len(users_word_1) < 7:
                print( f"\n jajaja ... The aim is to create a strong password. Thus we need a longer word. Your first password has {len(users_word_1)} letters. So this word should have at least {7-len(users_word_1)} letters. Try another word")
                time.sleep(3)
                users_word_1 = input("Please type in your word:")
        users_actual_words["SECOND_WORD"] = users_word_2.upper()
        user_words_modified["SECOND_WORD"] = users_actual_words["SECOND_WORD"]

        time.sleep(1)
        return "\n ______CALCULATING______"


# Execution the function "questions_to_user()"
print(questions_to_user())
time.sleep(1)


def Modify_Words():
    """
    # A function that modifies the users words (saved in the global variables FIRST_WORD and SECOND_WORD). In this
      process the words are transformed into leetspeak (using the dictionary), the SECOND_WORD is reversed and lowers
      all the characters of the words.
    """
    user_words_modified["FIRST_WORD"] = user_words_modified["FIRST_WORD"].lower()
    user_words_modified["FIRST_WORD"] = user_words_modified["FIRST_WORD"].capitalize()

    user_words_modified["SECOND_WORD"] = user_words_modified["SECOND_WORD"][::-1]
    user_words_modified["SECOND_WORD"] = user_words_modified["SECOND_WORD"].lower()
    user_words_modified["SECOND_WORD"] = user_words_modified["SECOND_WORD"].capitalize()

    for x, y in leetspeak_dictionary.items():
        user_words_modified["FIRST_WORD"] = user_words_modified["FIRST_WORD"].replace(x, str(y))
        user_words_modified["SECOND_WORD"] = user_words_modified["SECOND_WORD"].replace(x, str(y))
    time.sleep(1)
    (time.sleep(1))
    return "\n ______A MOMENT______"


# Execution of the function "Modify_Words"
print(Modify_Words())
time.sleep(2)

# Generation of a special character to which will be also included to the new password
special_characters = string.punctuation

# The modified global variables ("FIRST_WORD") and ("SECOND_WORD") will be merged to a password and the generated
# special character is between the two words (Structure: "FIRST_WORD + SPECIAL_CHARACTER + SECOND_WORD").
#       The personal words will be saved in global variables
new_password = user_words_modified["FIRST_WORD"] + random.choice(string.punctuation) + user_words_modified["SECOND_WORD"]


# Explanation of the generated password to the user

# Show the words picked by user
print(f"\n _____________________________________________________")
print("\n We are done. Now a short explanation of your password:")
first_word = users_actual_words["FIRST_WORD"]
second_word = users_actual_words["SECOND_WORD"]
print(f"\n Your first word was: {FIRST_WORD} and your second word was {SECOND_WORD}")
input("Press Enter to continue...")

# Show the change of the picked words after modification (leetspeak translation and  lower letters)
print("\n _____________________________________________________")
print(f"\n While the first letter of your words were turned into capitals, the rest were turned into small caps.")
print(f"\n Small caps were turned into leetspeak, if possible. ")
modified_FIRST_WORD = user_words_modified["FIRST_WORD"]
modified_SECOND_WORD = user_words_modified["SECOND_WORD"]
print(f"\n Original words:                    {FIRST_WORD} and {SECOND_WORD}")
print(f"\n Transformed words read as follows: {modified_FIRST_WORD} and {modified_SECOND_WORD[::-1]}")
input("Press Enter to continue...")

# Show additional modification to the second word (reverse of the second word)
print("\n _____________________________________________________")
print(f"\n As there leedspeak-encryptors that work in combination with dictionaries the second word is reversed.")
print(f"\n Transformed words: {modified_FIRST_WORD} and {modified_SECOND_WORD}")
input("Press Enter to continue...")

# Explanation that an addtional randomly generated special character was choosen and is place between the two words in
# the password
print("\n _____________________________________________________")
print(f"\n Finally we apply an additional recommendation of the german federal office to combine two words with a random special character.")
input("Press Enter to continue...")

# Show the actual password
print("\n _____________________________________________________")
print(f"\n So, your new password is :")
print(f"\033[1m{new_password}\033[1m")


# Link the user to a website to test the new password
input("Press Enter to test your new password")
import webbrowser
webbrowser.open("http://www.passwordmeter.com/")
