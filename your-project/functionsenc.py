import sys

#choicestring = ''
#choice = input('Type 0 to encrypt or 1 to decrypt: ')

def enc_or_dec(choice):
    choicestring = ''

    options = [0,1]
    if choice.isnumeric():
        choice = int(choice)
        if choice not in options:
            print("Your input is numeric but not '0' or '1'.")
            sys.exit()
        else:
            if choice == 0:
                choicestring = 'encrypt'
            else:
                choicestring = 'decrypt'
    else:
        print('ERROR! Your input is not numeric.')
        sys.exit()
    return (choicestring)

def intext(x):
    inserttext = f'Insert the text you want to {x}: '
    text = input(inserttext)
    return text



