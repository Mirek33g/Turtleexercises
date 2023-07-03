import turtle as t
import random


def random_move():
  tim = t.Turtle()

  colors = ["red", "blue", "green", "black"]
  directions = [0, 90, 180, 270]

  for i in range(200):
    tim.width(random.randint(0, 10))
    tim.speed(2)
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colors))
