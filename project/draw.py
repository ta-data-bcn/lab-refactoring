# Define Hangman drawings for turtle library
def draw_hangman_piece(piece, pen):
    if piece == 7:
        for it in range(2):
            pen.left(90)
            pen.forward(250)
    elif piece == 6:
        pen.left(90)
        pen.forward(25)
        pen.right(90)
        pen.circle(25)
    elif piece == 5:
        pen.penup()
        pen.left(90)
        pen.forward(50)
        pen.pendown()
        pen.forward(105)
    elif piece == 4:
        pen.penup()
        pen.right(180)
        pen.forward(70)
        pen.pendown()
        pen.left(135)
        pen.forward(60)
    elif piece == 3:
        pen.right(180)
        pen.penup()
        pen.forward(60)
        pen.right(90)
        pen.pendown()
        pen.forward(60)
    elif piece == 2:
        pen.penup()
        pen.right(180)
        pen.forward(60)
        pen.left(135)
        pen.forward(70)
        pen.right(45)
        pen.pendown()
        pen.forward(60)
    elif piece == 1:
        pen.right(180)
        pen.penup()
        pen.forward(60)
        pen.right(90)
        pen.pendown()
        pen.forward(60)
