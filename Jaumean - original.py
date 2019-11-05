import string
import random
import re

#The translator works by connecting characters of two lists, which will have different indexes.
#The difference of indexes will make the output change from one language to another.
#We create a list of accepted characters, in this case from ASCI 32-135 to keep input flexible.
lan_char = list(map(chr, range(32, 135)))

#Jaumean language will have the same characters as the other languages, so we copy the list.
jau_char = list.copy(lan_char)

#In order to change the order of the elements in the list, we pop an element and we append another one
#This is done to keep the same length between both lists.
jau_char.pop(1)
jau_char.append("a")

#EASTER EGG CODE because life is too short for not having Easter eggs telling you how awesome you are.
easter_egg = {
"Jaume": "The hottest smartest coolest man on Earth",
"Labs": "How many left to heaven?",
"Jaumean": "Also known as the best language in the world"
}

def welcome():
    print('WELCOME to JAUMEAN OFFICIAL TRANSLATOR.')
    #The program adapts depending on the language to/from translate. It is not case sensitive.
    options = {"TOJAU","TOLAN"}
    print('Typing TOJAU will translate your text to Jaumean, TOLAN will translate Jaumean text to your language.')
    user_language = input('Please type TOJAU or TOLAN to choose in which direction you want to translate:')
    user_language = user_language.upper()
    #If user inputs something different than any combination of ToJau or TOLan it will ask the user to do it again with instructions.
    if user_language not in options:
        print("\n"'Hey ~€€#~¬#~¬! Choose TOJAU to translate your language to Jaumean/n Choose TOLAN to translate from Jaumean to your language'"\n")
        user_language = input("\n"'Please type TOJAU or TOLAN to choose in which direction you want to translate,'"\n")
    return user_language

#Once the user has chosen in which direction to translate, the program runs until it presses Control + C
while True:
    user_language = welcome()
    if user_language == 'TOJAU':
        user_input = str(input('Please write the text you want to translate into Jaumean:'))
        #We create an empty list to contain the future output.
        jau_out = list()
        if user_input in easter_egg:
            jau_out.append(easter_egg[user_input])
        #The program identifies each character and space of the input and cuts it into single characters.
        input_list = re.findall('[\w ]',user_input)
        #Then it runs a loop where it finds the original language index into the list and find its connection to the other language one.
        for i in input_list:
            if user_input in easter_egg:
                break
            if i in lan_char:
                lan_ind = int(lan_char.index(i))
                #And it appends each new character into the output list.
                jau_out.append(jau_char[lan_ind])
        #The key here is that the output list is a group of separate characters, in order to print the list in the right format...
        #We use the *output_list sep = '' to make the program print all the output list as together, respecting spaces as well.
        print("\n"'Your text in Jaumean is: ', *jau_out, "\n",sep = '')
        print('If you want to finish press Control + C'"\n")

 #Same procedure with the TOLAN option.       
    if user_language == 'TOLAN':
        user_input = input('Please write the text you want to translate from Jaumean into your language:')
        input_list = re.findall('[\w ]',user_input)
        lan_out = list()
        for i in input_list:
            if i in jau_char:
                jau_ind = int(jau_char.index(i))
                lan_out.append(lan_char[jau_ind])
        print("\n"'The translation to your language is: ', *lan_out, "\n",sep = '')
        print('If you want to finish press Control + C'"\n")

