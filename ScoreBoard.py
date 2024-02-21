from turtle import Turtle
FONT = ("Comic Sans MS", 14, "bold")


class Board(Turtle):
    def __init__(self, session, global_):
        self.score = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 260)
        self.create()
        create(session, global_)

    def update(self, step=1):
        self.score += step
        self.clear()
        self.create()

    def create(self):
        self.write(f"Your Score: {self.score} -", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over !!", align="center")


def create(session_score, global_score):
    board = Turtle()
    board.penup()
    board.hideturtle()
    board.color("white")
    board.setpos(-180, 260)
    board.write(f"Your high score is: {session_score} -", align="center", font=FONT)
    board.goto(180, 260)
    board.write(f"Your best score is: {global_score}", align="center", font=FONT)
