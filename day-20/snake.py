from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SNAKE = 10

#DIRECTION IN DEGREES
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        self.full_snake.append(new_segment)
    
    def extend(self):
        self.add_segment(self.full_snake[-1].position())
            
    def move_snake(self):
        for snake_piece in range(len(self.full_snake) - 1, 0, -1):
            new_x = self.full_snake[snake_piece - 1].xcor()
            new_y = self.full_snake[snake_piece - 1].ycor()
            self.full_snake[snake_piece].goto(new_x, new_y)
        self.head.forward(MOVE_SNAKE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)