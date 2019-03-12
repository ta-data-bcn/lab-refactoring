import random

options = ['blue', 'green', 'red', 'yellow', 'white', 'black']
tries = 10

def machine_picks_colors():
    code = random.choices(options, k=4)
    print(f'Computer\'s randomized code is: {code}')
    return code

def player_picks_colors():
    colors = []
    while len(colors) < 4:
        choice = input(f"Choose one color from {options} and type it (position {len(colors)+1})")
        if choice in options:
            colors.append(choice)
        else:
            print('Type a color:')
    print(f"You're code is: {colors}")
    return colors

machine_code = machine_picks_colors()

for i in range(tries):
    
    person_guess = player_picks_colors()
    
    if person_guess == machine_code:
        print("You win")
        break
        
    for i in range(len(person_guess)):
        if person_guess[i] == machine_code[i]:
            print(1)
        elif person_guess[i] in machine_code:
            print(0)
        else:
            print('-')

        
    tries -= 1
    print(f"You have {tries} tries left")
    
    if tries == 0:
        print(f"You lost. The code was {machine_code}")