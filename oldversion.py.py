n_characters = input("How many digits do you want your password to have? '(at least 15 for safety reasons)' ")
def ask_for_length(n_characters):
    try:
        n_characters = int(n_characters)
        if n_characters < 15:
            print("This is less than 15, make it difficult for bored hackers, please try again")
            n_characters = 0
        elif n_characters > 20:
            print("Are you sure you want such a long password? You'll lose precious time that you could spend home doing nothing")
            n_characters = 0
        else:
            print(" Okey, ", int(n_characters), " sounds like a good length")
    except ValueError:
        print( n_characters, " It's not a number, Smart Ass ")
        n_characters = 0
    return int(n_characters)  

user_input = ask_for_length(n_characters)

characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(user_input))
name = input("what's your name? ")
def Is_your_name_in_Password(name):
    print(name in password)
    return
print("Here is your new and super secure Password: ", password)
print("Is your name in the password?")
name_input = str(Is_your_name_in_Password(name))
print("Feel free to copy it and paste it where it rightfully goes.")