from string import ascii_letters, ascii_lowercase
from random import randint

weak_lst = ascii_lowercase
intermediate_lst = ascii_letters
strong_lst = ascii_letters + '0123456789'
pass_lst = []


def readable(word):
    """
    Get a string from user, transforms it into another string and print the password.
    :param word : str
    :return No return (shows password in console with print):
    """
    readable_dict = {"s": "5", "S": "5", "b": "8", "B": "8", "e": "3", "E": "3", "i": "1", "I": "1", "a": "@",
                     "A": "@", "o": "0", "O": "0", "t": "7", "T": "7", " ": ""}
    pass_str = word
    for char in word:
        if char in readable_dict.keys():
            pass_str = pass_str.replace(char, readable_dict[char])
    print(f'Your readable strong password is: -{pass_str}.')


def weak(num):
    """
    Get a number from the user, and use it to define the length of the password (Minimum length 8, maximum 16)
    print a random password of lower case letters.
    :param num : int
    :return No return (shows password in console with print):
    """
    if int(num) <= 8:
        num = 8
    for char in range(num):
        pass_lst.append(weak_lst[randint(0, len(weak_lst)-1)])
    pass_str = "".join(pass_lst)
    print(f'Your weak password is: {pass_str}')


def intermediate(num):
    """
    Get a number from the user, and use it to define the length of the password (Minimum length 8, maximum 16)
    print a random password of lower and upper letters. Check if there is an upper letter in the password, if not
    just call the function again (recursive function).
    :param num : int
    :return No return (shows password in console with print):
    """
    if int(num) <= 8:
        num = 8
    pass_check = 0
    pass_lst = []
    pass_str = ""
    for char in range(num):
        pass_lst.append(intermediate_lst[randint(0,len(intermediate_lst)-1)])
    pass_str = "".join(pass_lst)
    for char in pass_str:
        if char in intermediate_lst[26:]:
            pass_check += 1
    if pass_check >= 1:
           print(f'Your intermediate password is: {pass_str}')
    else:
        intermediate(num)


def strong(num):
    """
    Get a number from the user, and use it to define the length of the password (Minimum length 8, maximum 16)
    print a random password of lower, upper letters and numbers. Check if there is a number in the password, if
    not just call the function again (recursive function).
    :param num : int
    :return No return (shows password in console with print):
    """
    if int(num) <= 8:
        num = 8
    pass_check = 0
    pass_lst = []
    pass_str = ""
    for char in range(num):
        pass_lst.append(strong_lst[randint(0, len(strong_lst)-1)])
    pass_str = "".join(pass_lst)
    for char in pass_str:
        if char in strong_lst[52:]:
            pass_check += 1
    if pass_check >= 1:
           print(f'Your strong password is: {pass_str}')
    else:
        strong(num)

