# Module for drawing the hangman

# Three hangman draws with different shapes to be printed for different word lengths.
# For words between shorter than 6 chars, max_mistakes is 5 and the draw_1 is printed.
# For words between 6 and 8 chars, max_mistakes is 7 and the draw_2 is printed.
# For words longer than 8 chars, max_mistakes is 9 and the draw_3 is printed.

draw_1 = '''                           |------_
                                 |_| 
                                --|--
                                  |                                          
                                 / \\'''
# (n = 5)

draw_2 = '''                           |------
                                  |
                                  _
                                 |_| 
                                --|--
                                  |                                          
                                 / \\'''
# (n = 7)

draw_3 = '''                           |------
                                  |
                                  |
                                  |
                                  |
                                  _
                                 |_| 
                                --|--
                                  |                                          
                                 / \\'''
# (n = 9)


def draw_hangman(max_mistakes, mistakes):
    '''Draws (prints) hangman depending on the initial number of mistakes (max_mistakes) and the current mistakes.'''
    if max_mistakes == 5:
        for m in range(mistakes):
            print(draw_1.split('\n')[m])
    elif max_mistakes == 7:
        for m in range(mistakes):
            print(draw_2.split('\n')[m])
    else:
        for m in range(mistakes):
            print(draw_3.split('\n')[m])
