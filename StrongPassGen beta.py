import string
import random
readable_dict = {"s":"5","S":"5","b":"8","B":"8","e":"3","E":"3","i":"1","I":"1","a":"@","A":"@","o":"0","O":"0","t":"7","T":"7"," ":""}
weak_lst = string.ascii_lowercase
interm_lst = string.ascii_letters
strong_lst = interm_lst + '0123456789'
premium_lst = strong_lst + '#@-.$*()+;:/%_?,=&!'
pass_lst = []
pass_str = ""
pass_check = 0
option = ""
num = ""

def start():
    print("""Welcome to the ultimate strong password generator®
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
                readable(word)
            if int(option) == 2 or int(option) == 3 or int(option) == 4 or int(option) == 5:
                num = input('How long do you want your password? (Will have atleast 8 characters and SHOULD BE lower or equal to 16) ')
                if num.isnumeric():
                    if int(num) <= 16:
                        if int(option) == 2:
                            weak(int(num))
                        if int(option) == 3:
                            intermediate(int(num))
                        if int(option) == 4:
                            strong(int(num))
                        if int(option) == 5:
                            premium(int(num))
                    else:
                        print('Next time provide a number lower or equal 16')
                else:
                    print('Next time provide a number :(')
            if int(option) == 6:
                word = input('Please provide me a password: ')
                evaluate(word)
        else:
            print('Next time provide a correct option :(')
    else:
        print('Next time provide a correct option :(')

def readable(word):
    pass_str = word
    for char in word:
        if char in readable_dict.keys():
            pass_str = pass_str.replace(char,readable_dict[char])
    print(f'Your readable strong password is: -{pass_str}.')

def weak(num):
    if int(num) <= 8:
        num = 8
    for char in range(num):
        pass_lst.append(weak_lst[random.randint(0,len(weak_lst)-1)])
    pass_str = "".join(pass_lst)
    print(f'Your weak password is: {pass_str}')

def intermediate(num):
    if int(num) <= 8:
        num = 8
    pass_check = 0
    pass_lst = []
    pass_str = ""
    for char in range(num):
        pass_lst.append(interm_lst[random.randint(0,len(interm_lst)-1)])
    pass_str = "".join(pass_lst)
    #Check if it has some upper case letter, if not just call the function again
    for char in pass_str:
        if char in interm_lst[26:]:
            pass_check += 1
    if pass_check >= 1:
           print(f'Your intermediate password is: {pass_str}')
    else:
        intermediate(num)

def strong(num):
    if int(num) <= 8:
        num = 8
    pass_check = 0
    pass_lst = []
    pass_str = ""
    for char in range(num):
        pass_lst.append(strong_lst[random.randint(0,len(strong_lst)-1)])
    pass_str = "".join(pass_lst)
    #Check if it has some number, if not just call the function again
    for char in pass_str:
        if char in strong_lst[52:]:
            pass_check += 1
    if pass_check >= 1:
           print(f'Your strong password is: {pass_str}')
    else:
        strong(num)

def premium(num):
    if int(num) <= 8:
        num = 8
    pass_check = 0
    pass_lst = []
    pass_str = ""
    for char in range(num):
        pass_lst.append(premium_lst[random.randint(0,len(premium_lst)-1)])
    pass_str = "".join(pass_lst)
    #Check if it has some non-alph char, if not just call the function again
    for char in pass_str:
        if char in premium_lst[62:]:
            pass_check += 1
    if pass_check >= 1:
           print(f'Your premium password is: {pass_str}')
    else:
        premium(num)

def evaluate(word):
    evaluate_upper = 0
    evaluate_number = 0
    evaluate_non_alpha = 0
    evaluate_len = 0
    evaluate_total = 0
    if len(word) >= 8:
        evaluate_len += 1
    for char in word:
        if char in interm_lst[26:]:
            if evaluate_upper == 0:
                evaluate_upper += 1
        if char in strong_lst[52:]:
            if evaluate_number == 0:
                evaluate_number += 1
        if char in premium_lst[62:]:
            if evaluate_non_alpha == 0:
                evaluate_non_alpha +=1
    evaluate_total = evaluate_upper + evaluate_number + evaluate_non_alpha + evaluate_len
    if evaluate_total == 4:
        print('You have the ULTIMATE password security. Not even the NSA can get your email!')
    if evaluate_total == 3:
        print('You have a strong password security')
    if evaluate_total == 2:
        print('You have a intermediate password security')
    if evaluate_total == 1:
        print('You have a weak password security')
    if evaluate_total == 0:
        print('You should use this program to generate a good password! (Your password is really weak)')

start()