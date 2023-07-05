import turtle as t
import random
from figure import random_color

tim = t.Turtle()
tim.hideturtle()
tim.penup()
t.colormode(255)

tim.setheading(220)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

nr_dots = 100


def dots():
  for i in range(1, nr_dots + 1):
    tim.dot(20, random_color())
    tim.forward(45)
    if i % 10 == 0:
      tim.setheading(90)
      tim.forward(45)
      tim.setheading(180)
      tim.forward(450)
      tim.setheading(0)
