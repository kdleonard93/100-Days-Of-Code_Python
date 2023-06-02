from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=550, height=500)
user_bets = screen.textinput(title="Make your bet!", prompt="Who will win the race? Pick your color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [100, 50, 0, -50, -100, -150]
all_turtles = []
    

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)
    print(all_turtles)
    
if user_bets:
    race_on = True
    
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 255:
            race_on = False
            winning_color = turtle.pencolor()
            if  winning_color == user_bets:
                print(f"You won the race with {winning_color}!")
            else:
                print(f"You lost the race with {winning_color}!")
                
        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)
        


screen.exitonclick()