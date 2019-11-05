import string
import random
import re
from list_creator import create_list
from easter_egg import easteregg
from welcome import hello

# The program connects characters of two different lists which include ASCI characters.
create_list()

#EASTER EGG CODE because life is too short for not having Easter eggs telling you how awesome you are.
easteregg()

#The program adapts depending on the language to/from translate. It is not case sensitive.
hello()

# The program create an empty list, identifies each character from the input and find its equivalent.
while True:
    user_language = hello()
    if user_language == 'TOJAU':
        user_input = str(input('Please write the text you want to translate into Jaumean:'))
        jau_out = list()
        if user_input in easter_egg:
            jau_out.append(easter_egg[user_input])
        input_list = re.findall('[\w ]',user_input)
        for i in input_list:
            if user_input in easter_egg:
                break
            if i in lan_char:
                lan_ind = int(lan_char.index(i))
                #And it appends each new character into the output list.
                jau_out.append(jau_char[lan_ind])
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

