from turtle import Turtle, Screen
import random

tim = Turtle()

screen = Screen()
screen.colormode(255)
directions = [0, 90, 180, 270,]
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(360):
    tim.color(random_color())
    tim.circle(100)
    tim.right(1)
    
screen.exitonclick()


