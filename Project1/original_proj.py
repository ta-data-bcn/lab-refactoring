import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789+-*/<>!¡?¿@|#$€%&=-_'
password_lenght = 0
while password_lenght < 8:
    password_lenght = int(input('password lenght (8 characters minimum): '))


number_of_passwords = int(input('How many passwords you want?: '))


for i in range(number_of_passwords):
    password = random.choice(characters)

    for char in range(1, password_lenght):
        password += random.choice(characters)
        while password[char] == password[char-1]:
            password = password[:-1]
            password += random.choice(characters)
    print (password)
