# Function to roll dice

def rolldice():
    import random
    return random.randint(1,6)


# Yes or no function

def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")


# Functions to create both pool of dice

def dice_roll(pool):
    pool_dice = []
    for dice in range(pool):
        pool_dice.append(rolldice())
    return pool_dice


def pooling(dice_a, dice_d) :
    if dice_a > 3: # Attacker can only field 3 soldiers
        pool_a = dice_roll(3)
    else:
        pool_a = dice_roll(dice_a - 1) # Attacker has to leave one soldier on the land he comes from
    pool_a.sort(reverse=True)
    
    if dice_d > 2: # Defender can only field 2 defenders
        pool_d = dice_roll(2)
    else:
        pool_d = dice_roll(defend)
    pool_d.sort(reverse=True)
    
    return pool_a, pool_d
# Both pools have been sorted and reversed as we have to compare from the highest scores.


# Function to compare dice rolls and update the scores

def compare_pool(pool_a, pool_d, attack, defend):
    for i in range(min(len(pool_a), len(pool_d))):
        if pool_a[i] > pool_d[i]:
            defend += -1 # Attacker wins
        else:
            attack += -1 # Defender wins
    return (attack, defend)


# #### Setup the armies

def setup_armies():
    attack = input('How many soldiers are in the attacking land? ')
    while not attack.isdigit(): # checking for right input
        attack = input('How many soldiers are in the attacking land? ')
    defend = input('How many soldiers are defending the land? ')
    while not defend.isdigit(): # checking for right input
        defend = input('How many soldiers are defending the land? ')
    attack = int(attack)
    defend = int(defend)
    return attack, defend


# #### Fight round

def fight(attack, defend):
    charge = True
    while charge:
        if attack > 1 and defend > 0:
            pool_attack, pool_defend = pooling(attack,defend)
            (attack, defend) = compare_pool(pool_attack, pool_defend, attack, defend)
        elif attack <= 1: # Attacker has to leave one soldier in the land he attacks from
            print('You have no more troops to attack.')
            charge = False
        else:
            print('You have conquered the land!')
            charge = False
        if attack > 1 and defend > 0: # Checking for a new round. 'y' will work, any other letter will quit the game.
            charge = yes_or_no('You can try attacking again with {0} against {1} defenders.'.format(attack, defend))



