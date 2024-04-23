import turtle

def drawPoly(t, n, sz):

    ca = 180 - (((n - 2) / n) * 180)
    
    for i in range(n):
        t.forward(sz)
        t.left(ca)


wn = turtle.Screen()
wn.bgcolor("lime green")

alex = turtle.Turtle()
alex.color("firebrick")
alex.pensize(5)

corners = int(input("How many Corners should it habe? "))
size = int(input("How long should one side be? "))

drawPoly(alex, corners, size)

wn.exitonclick()