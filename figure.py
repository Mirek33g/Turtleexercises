import turtle as t
import random


def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  colors = (r, g, b)
  return colors


def figures():
  tim = t.Turtle()
  tim.speed(1)
  t.colormode(255)
  b = 3

  def draw(a):
    for i in range(a):
      tim.forward(50)
      tim.right(360 / a)

  for i in range(b, 12):
    tim.color(random_color())
    draw(b)
    b += 1
