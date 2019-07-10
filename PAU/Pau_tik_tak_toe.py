#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Define the grid and coordinates
import random

def print_updated_grid():
    for i in grid:
        print(i)
    print("\n")

def func_random():
    x = random.choice(coordinates)
    return x

def select_move_player():
    for x in range (3):
        select_row = input("Enter your choice: (type 0,1 or 2 for rows coordinates) you have 3 tries if not you lose your round: ")
        select_column = input("Enter your choice: (type 0,1 or 2 for columns coordinates) you have 3 tries if not you lose your round: ")
        if select_row and select_column in coordinates:
            r = int(select_row)
            c = int(select_column)
            if grid[r][c] == " ":
                grid[r][c] = "X"
                return r,c
            else:
                print("This spot is full")
        else:
            print("Try again")

def select_move_machine():
    for x in range (10):
        select_row = func_random()
        select_column = func_random()
        if select_row and select_column in coordinates:
            r = int(select_row)
            c = int(select_column)
            if grid[r][c] == " ":
                grid[r][c] = "O"
                return r,c
        else:
            print("Try again")

def checking_winner():
    for i in to_win_comb:
        if i == winner_comb_player:
            print("Player won")
        elif i == winner_comb_machine:
            print("Machine won")

def check_hor():
    a = "over"
    for i in grid:
        c0 = i[0]
        c1 = i[1]
        c2 = i[2]
        if c0 == c1 == c2 and (c0 != " ") and (c1 != " ") and (c2 != " ") and (c0 == "X") and (c1 == "X") and (c2 == "X"):
            print("player WIN horizontal")
            return a
        elif c0 == c1 == c2 and (c0 != " ") and (c1 != " ") and (c2 != " ") and (c0 == "O") and (c1 == "O") and (c2 == "O"):
            print("machine WIN horizontal")
            return a

def check_ver():
    a = "over"
    lst0 = []
    lst1 = []
    lst2 = []
    for i in grid:
        lst0.append(i[0])
        lst1.append(i[1])
        lst2.append(i[2])
    provi = [lst0,lst1,lst2]
    check_hor()

def check_diag():
    a = "over"
    d0 = grid[0][0]
    d1 = grid[1][1]
    d2 = grid[2][2]
    if d0 == d1 == d2 and (d0 != " ") and (d1 != " ") and (d2 != " ") and (d0 == "X") and (d1 == "X") and (d2 == "X"):
            print("player WIN diagonal")
            return a
    elif d0 == d1 == d2 and (d0 != " ") and (d1 != " ") and (d2 != " ") and (d0 == "O") and (d1 == "O") and (d2 == "O"):
            print("machine WIN diagonal")
            return a

def check_diag2():
    a = "over"
    d0 = grid[2][0]
    d1 = grid[1][1]
    d2 = grid[0][2]
    if d0 == d1 == d2 and (d0 != " ") and (d1 != " ") and (d2 != " ") and (d0 == "X") and (d1 == "X") and (d2 == "X"):
            print("player WIN diagonal")
            return a
    elif d0 == d1 == d2 and (d0 != " ") and (d1 != " ") and (d2 != " ") and (d0 == "O") and (d1 == "O") and (d2 == "O"):
            print("machine WIN diagonal")
            return a

def main():
    print("Welcome to the Tic-Tac-Toe game")
    for i in range(5):
        select_move_player()
        print_updated_grid()
        a = check_hor()
        b = check_ver()
        c = check_diag()
        d = check_diag2()
        if a or b or c or d == "over":
            break
        select_move_machine()
        print_updated_grid()
        e = check_hor()
        f = check_ver()
        g = check_diag()
        h = check_diag2()
        if e or f or g or h == "over":
            break

for i in range(3):
    for i in range(5):
        answer = input("Do you want to play Tic-Tac-Toe game? [y/n]: if you write another letter the game ends")
        if answer == "y":

            grid = [[" "," "," "],
                    [" "," "," "],
                    [" "," "," "]]

            coordinates = ["0","1","2"]

            main()

        elif answer == "n":
            break
        break
    break


# In[ ]:



