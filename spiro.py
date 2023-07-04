import turtle as t
from figure import random_color

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)


def spirograph():

  def draw(size):
    for i in range(int(360 / size)):
      tim.color(random_color())
      tim.setheading(tim.heading() + 10)
      tim.circle(100)

  draw(10)
