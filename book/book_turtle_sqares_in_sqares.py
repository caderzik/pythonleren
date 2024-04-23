import turtle

def drawSquare(t, sz):

    for i in range(4):
        t.forward(sz)
        t.left(90)  

    

    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lime green")

alex = turtle.Turtle()
alex.color("firebrick")
alex.pensize(5)

squares = [100, 80, 60, 40, 20]

for i in squares:
    drawSquare(alex, i)

wn.exitonclick()