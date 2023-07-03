import turtle as t 
import random 

def figures():
  tim = t.Turtle()
  b = 3
  colors = ["red", "blue", "green", "purple", "orange", "yellow", "black"]

  def draw(a):
    for i in range(a):
      tim.forward(50)
      tim.right(360 / a)

  for i in range(b, 12):
    tim.color(random.choice(colors))
    draw(b)
    b += 1
