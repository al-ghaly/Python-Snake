from turtle import Turtle

POSITIONING = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.head = None
        self.tail = None
        self.create_snake()
        self.head.color("red")

    def create_snake(self):
        for position in POSITIONING:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.setpos(position)
        segment.color("white")
        self.segments.append(segment)
        self.tail = self.segments[-1]

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            pos = self.segments[segment - 1].pos()
            self.segments[segment].goto(pos)
            head = self.segments[segment - 1].heading()
            self.segments[segment].setheading(head)
        self.head.forward(STEP)

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

    def grow(self):
        self.add_segment(self.tail.position())

    def detect(self):
        if self.head.xcor() > 290 or self.head.xcor() < -280 or self.head.ycor() > 300 or self.head.ycor() < -290:
            return True
        return self.collision()

    def collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
