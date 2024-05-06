import turtle

def drawSquare(t, sz):

    for i in range(4):
        t.forward(sz)
        t.left(90)
    
    angle = 18
    t.left(angle)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
for i in range(20):
    drawSquare(alex,50)

wn.exitonclick()