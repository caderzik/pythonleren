# for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
#     print("Hi", name, "Please come to my party on Saturday!")

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

# for i in [0, 1, 2, 3]:
#     alex.forward(50)
#     alex.left(90)

for i in range(4):
    alex.forward(50)
    alex.left(90)

wn.exitonclick()