from turtle import Turtle, Screen
import random


def race():
  is_race_on = False

  screen = Screen()
  screen.setup(width=600, height=400)
  user_bet = screen.textinput(title= "Make your bet", prompt= "Which turte will win the race? Type a color: ")
  print(user_bet)
  colors = ["yellow", "green", "red", "purple", "blue", "black"]
  position = [-125, -75, -25, 25, 75, 125]
  all_turtles = []

  for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-580, position[i])
    all_turtles.append(new_turtle)

  if user_bet:
    is_race_on = True

  while is_race_on:
    for t in all_turtles:
      if t.xcor() > 595:
        is_race_on = False
        winner = t.pencolor()
        if winner == user_bet:
          print(f"You have won! The {winner} turtle is the winner")
        else:
          print(f"Youe have lost. The {winner} turtle is the winner")

      distance = random.randint(0, 10)
      t.forward(distance)
