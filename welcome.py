#The program adapts depending on the language to/from translate. It is not case sensitive.
def hello():
    print('WELCOME to JAUMEAN OFFICIAL TRANSLATOR.')
    options = {"TOJAU","TOLAN"}
    print('Typing TOJAU will translate your text to Jaumean, TOLAN will translate Jaumean text to your language.')
    user_language = input('Please type TOJAU or TOLAN to choose in which direction you want to translate:')
    user_language = user_language.upper()
    if user_language not in options:
        print("\n"'Hey ~€€#~¬#~¬! Choose TOJAU to translate your language to Jaumean/n Choose TOLAN to translate from Jaumean to your language'"\n")
        user_language = input("\n"'Please type TOJAU or TOLAN to choose in which direction you want to translate,'"\n")
    return user_language
