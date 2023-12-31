from turtle import Turtle
up = 90
down = 270
left = 180
right = 0
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def reset(self):
        for segment in self.segments:
            segment.goto(500,500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.seth(up)

    def down(self):
        if self.head.heading() != up:
            self.head.seth(down)

    def left(self):
        if self.head.heading() != right:
            self.head.seth(left)

    def right(self):
        if self.head.heading() != left:
            self.head.seth(right)
