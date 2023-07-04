import turtle as t
import random
from figure import random_color


def random_move():
  tim = t.Turtle()
  t.colormode(255)
  tim.speed(1)

  directions = [0, 90, 180, 270]

  for i in range(200):
    tim.width(random.randint(1, 5))
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random_color())
