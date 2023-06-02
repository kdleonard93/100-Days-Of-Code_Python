from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    
def move_backwards():
    tim.back(10)
    
def counter_clockwise():
    tim.left(10)
    
def clockwise():
    tim.right(10)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="d", fun=move_forward)
screen.onkey(key="a", fun=move_backwards)
screen.onkey(key="w", fun=counter_clockwise)
screen.onkey(key="s", fun=clockwise)
screen.onkey(key="c", fun=clear)



screen.exitonclick()