import FreeVersion as fv
import PaidVersion as pv


def start():
    print("""Welcome to the Ultimate Strong Password Generator®
    You have 6 options:
    1. Generate an easy password to remember
    2. Generate a weak password
    3. Generate a intermediate password
    4. Generate a strong password
    Premium options (4.99€):
    5. Generate a premium password
    6. Evaluate a password""")

    option = input('Choose your option (1 to 6): ')
    if option.isnumeric():
        if int(option) <= 6:
            if int(option) == 1:
                word = input('Please provide me a word: ')
                fv.readable(word)
            if int(option) == 2 or int(option) == 3 or int(option) == 4 or int(option) == 5:
                num = input('How long do you want your password? (Will have atleast 8 characters and '
                            'SHOULD BE lower or equal to 16) ')
                if num.isnumeric():
                    if int(num) <= 16:
                        if int(option) == 2:
                            fv.weak(int(num))
                        if int(option) == 3:
                            fv.intermediate(int(num))
                        if int(option) == 4:
                            fv.strong(int(num))
                        if int(option) == 5:
                            pv.premium(int(num))
                    else:
                        print('Next time provide a number lower or equal 16')
                else:
                    print('Next time provide a number :(')
            if int(option) == 6:
                word = input('Please provide me a password: ')
                pv.evaluate(word)
        else:
            print('Next time provide a correct option :(')
    else:
        print('Next time provide a correct option :(')


start()
