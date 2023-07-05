from turtle import Turtle, Screen
import random 




def race():
  
  screen = Screen() 
  screen.setup(width= 800, height= 550) 
  #user_bet = screen.textinput(title= "Make your bet", prompt= "Which turte will win the race? Type a color: ")
 # print(user_bet)



  pac = Turtle("turtle")
  pac.penup()
  pac.color("yellow")
  pac.goto(-380, 150)

  pic = Turtle("turtle")
  pic.penup()
  pic.color("green")
  pic.goto(-380, 75)
  
  tim = Turtle("turtle")
  tim.penup()
  tim.color("red")
  tim.goto(-380, 0) 

  tom = Turtle("turtle")
  tom.penup() 
  tom.color("blue")
  tom.goto(-380, -75)

  ben = Turtle("turtle")
  ben.penup()
  ben.color("purple")
  ben.goto(-380, -150)









