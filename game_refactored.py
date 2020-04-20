from userName import username
from chooseLevel import which_level
import levels
from cpuNumber import computer_number


def guess_number(cpu):
    (number, tries) = cpu
    u_number = None
    for i in range(1, (tries + 1)):
        while type(u_number) != int:
            try:
                u_number = int(input('Which number do you want to try? \n'))
                break
            except ValueError:
                print('Write an integer number')

        if u_number < number:
            print(f'Is greater than {u_number}, you have {tries - i} tries left')
            u_number = None
        elif u_number > number:
            print(f'Is lower than {u_number}, you have {tries - i} tries left')
            u_number = None
        else:
            print(f'Congrats! You guessed the number I thought!\nThe correct number was {u_number}\nYou tried {i} times')
            break

        if (tries) - i == 0:
            print(f'Good luck the next time, the number was {number}')



u_name = username()
l_chosen = which_level(u_name)
cpu = computer_number(l_chosen)
guess_number(cpu)