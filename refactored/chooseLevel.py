import levels

def which_level(username):
    option = 0
    while option == 0:
        level_input = input(f'Now you have to choose a level, \nWrite 1 or easy: {levels.levels["easy"][0]} tries and the number goes from {str(levels.levels["easy"][1])} to {str(levels.levels["easy"][2])} \nWrite 2 or medium: {levels.levels["medium"][0]} tries and the number goes from {str(levels.levels["medium"][1])} to {str(levels.levels["medium"][2])}\nWrite 3 or hard: {levels.levels["hard"][0]} tries and the number goes from {str(levels.levels["hard"][1])} to {str(levels.levels["hard"][2])} \n')

        try:
            val = int(level_input)
            if val in [1,2,3]:
                if val == 1:
                    level = "easy"
                    print(f'Congrats, {username}, you have chosen the level {level}')
                    option += 1
                elif val == 2:
                    level = "medium"
                    print(f'Congrats, {username}, you have chosen the level {level}')
                    option += 1
                else:
                    level = "hard"
                    print(f'Congrats, {username}, you have chosen the level {level}')
                    option += 1
        except ValueError:
            try:
                val = str(level_input).lower()
                if val in ['easy', 'medium', 'hard']:
                    if val == "easy":
                        level = "easy"
                        print(f'Congrats, {username}, you have chosen the level {level}')
                        option += 1
                    elif val == "medium":
                        level = "medium"
                        print(f'Congrats, {username}, you have chosen the level {level}')
                        option += 1
                    else:
                        level = "hard"
                        print(f'Congrats, {username}, you have chosen the level {level}')
                        option += 1
            finally:
                print("Try again")    


    return (level)
