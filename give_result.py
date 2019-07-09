## Define a function to give the result of a round:
### Black means the right colour in the right position
### White means this colour is present in the computer choice but in the wrong position
def give_result():
    """ This function gives the result of a round:
Black means the right colour in the right position
White means this colour is present in the computer choice but in the wrong position"""
    result = ["nothing", "nothing", "nothing", "nothing"]
    computer = list(computer_tuple)
    computer_bis = computer
    for i in range(len(player)):
        # Check if there are any Blacks in the results and add it to the list [b]
        if player[i] == computer[i]:
            result[i] = "black"
            computer_bis[i] = "taken"
    for i in range(len(player)):
        # Check if there are any Whites in the results and add it to the list [b]
        for j in range(len(computer)):
            if player[i] == computer_bis[j]:
                result[i] = "white"
                computer_bis[j] = "taken"
                break
    print(f"\nThe result is {result}\n")
    return result
