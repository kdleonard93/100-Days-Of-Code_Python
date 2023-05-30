from turtle import Turtle, Screen
import _tkinter
import random
import colorgram

tim_t = Turtle()
screen = Screen()
screen.colormode(255)
tim_t.speed(0)
color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]

tim_t.penup() # turtle starts with pen down by default, we start with lifting the pen up
tim_t.hideturtle() # hide the turtle

# setup starting position (top left corner)
start_x = -250
start_y = 250
tim_t.goto(start_x, start_y)

# draw the dots in a grid
dot_size = 20
spacing = 50 # space between dots

for y in range(start_y, start_y - 10 * spacing, -spacing):
    for x in range(start_x, start_x + 10 * spacing, spacing):
        tim_t.goto(x, y)
        tim_t.dot(dot_size, random.choice(color_list))
        
screen.exitonclick()


