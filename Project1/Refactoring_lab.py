import string
import random

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all_characters = string.printable
password_length = 0

while password_length < 8:
    password_length = int(input('-Password length (8 characters minimum): '))

number_of_passwords = int(input('-How many passwords do you want?: '))
type_of_password = input(
    '-Which kind of passwords do you want? (lowercase: l, uppercase: u, digits: d, symbols: s or any character: a): ')

while type_of_password not in 'ludsa':
    type_of_password = input(
        '-Which kind of passwords do you want? (lowercase: l, uppercase: u, digits: d, symbols: s or any character: a): ')

if type_of_password == 'l':
    type_of_password = lowercase

elif type_of_password == 'u':
    type_of_password = uppercase

elif type_of_password == 'd':
    type_of_password = digits

elif type_of_password == 's':
    type_of_password = symbols

elif type_of_password == 'a':
    type_of_password = all_characters


def Random_Password():
    password = ''.join(random.sample(type_of_password, password_length))
    return password


print(Random_Password())

#LIST COMPREHENSION, METER EL FOR GRAND EEN UNA FUNCION, AUMENTAR CODIGO, USAR LO DE LAS TRES COMILLAS
#AÑADIR COMENTARIOS, FIX ERRORS (NO VA SI NO DAS UN NUMERO), DO LIBRARIES?????????????????????????????