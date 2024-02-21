from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        self.move()
        
    def move(self):
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        self.goto(x, y)


class BetterFood(Food):
    def __init__(self):
        super().__init__()
        self.hideturtle()


class BestFood(BetterFood):
    def __init__(self):
        super().__init__()
