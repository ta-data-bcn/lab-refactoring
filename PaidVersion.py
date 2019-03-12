from string import ascii_letters
from random import randint

premium_lst = ascii_letters + '0123456789' + '#@-.$*()+;:/%_?,=&!'


def premium(num):
    """
    Get a number from the user, and use it to define the length of the password (Minimum length 8, maximum 16)
    print a random password of lower, upper letters, numbers and non-alphanumerical characters. Check if there is
    a non alphanumerical in the password, if not just call the function again (recursive function).
    :param num : int
    :return No return (shows password in console with print):
    """
    if int(num) <= 8:
        num = 8
    pass_check = 0
    pass_lst = []
    pass_str = ""
    for char in range(num):
        pass_lst.append(premium_lst[randint(0, len(premium_lst)-1)])
    pass_str = "".join(pass_lst)
    for char in pass_str:
        if char in premium_lst[62:]:
            pass_check += 1
    if pass_check >= 1:
            print(f'Your premium password is: {pass_str}')
    else:
        premium(num)


def evaluate(word):
    """
    Get a string(word) from the user to check if it could be a strong password. The function checks if there's some
    characters like upper letters, numbers, non-alphanumerical and the length of the string.
    :param word : str
    :return:
    """
    evaluate_upper = 0
    evaluate_number = 0
    evaluate_non_alpha = 0
    evaluate_len = 0
    if len(word) >= 8:
        evaluate_len += 1
    for char in word:
        if char in premium_lst[26:] and evaluate_upper == 0:
            evaluate_upper += 1
        if char in premium_lst[52:] and evaluate_number == 0:
            evaluate_number += 1
        if char in premium_lst[62:] and evaluate_non_alpha == 0:
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
