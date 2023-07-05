from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forwards():
  tim.forward(10)


def backwards():
  tim.backward(10)


def co_clockwise():
  tim.left(10)


def clockwise():
  tim.right(10)


def clear_screen():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()


def draw():
  screen._listen()
  screen.onkey(key="w", fun=forwards)
  screen.onkey(key="s", fun=backwards)
  screen.onkey(key="a", fun=co_clockwise)
  screen.onkey(key="d", fun=clockwise)
  screen.onkey(key="c", fun=clear_screen)
