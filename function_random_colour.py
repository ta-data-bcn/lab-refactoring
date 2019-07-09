## Define a random generator function to generate the computer choice of colours and positions
def random_colour():
    """ This function generates the computer choice of colours and positions"""
    a = [random.choice(colours) for i in range(4)]
    return (a)