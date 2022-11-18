# from turtle import Screen, Turtle

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

table.add_column("Pokemon Name",
                 ["Pika", "Char", "Squirt"])
table.add_column("Type",
                 ["Electric", "Fire", "Water"])

table.align = "l"

print(table)
