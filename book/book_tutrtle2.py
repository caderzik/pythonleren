import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)  
    t.penup()
    t.forward(sz * 2)
    t.pendown()
    return 0

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")
for i in range(5):
    drawSquare(alex,20)

wn.exitonclick()
