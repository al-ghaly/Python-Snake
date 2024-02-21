from turtle import Screen
from Snake import Snake
import time, sys, shelve
from Food import Food, BetterFood, BestFood
from ScoreBoard import Board

screen = Screen()
screen.setup(width=580, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

mapper_encode = {1: "jhfd", 2: "bdsuuhbds", 3: "cbhfd", 4: "hbcfd", 5: "bfhdvf",
                 6: "hdisufhi", 7: "fvduibvih", 8: "bvfdvb", 9: "hdsfig", 0: "jbndsbf"}

mapper_decode = {"jhfd": 1, "bdsuuhbds": 2, "cbhfd": 3, "hbcfd": 4, "bfhdvf": 5,
                 "hdisufhi": 6, "fvduibvih": 7, "bvfdvb": 8, "hdsfig": 9, "jbndsbf": 0}


def decrypt(string):
    decoded = ""
    words = string.split()
    for word in words:
        decoded += str(mapper_decode[word])
    return int(decoded)


scores = [0]
score = shelve.open("score")
maximum_score = decrypt(score["Ran"])
score.close()


def game():
    snake = Snake()
    food = Food()
    better_food = BetterFood()
    better_food.color("green")
    best_food = BestFood()
    best_food.color("yellow")
    board = Board(max(scores), maximum_score)

    message = "PLEASE ENTER THE GAME LEVEL : H --> FOR HARD M --> FOR MEDIUM E --> FOR EASY"

    while True:
        level = screen.textinput(title="Game Level", prompt=f"{message}")
        if level is None:
            return
        elif level.lower() == 'e' or level.lower() == 'm' or level.lower() == 'h':
            break
        else:
            message = "PLEASE ENTER A VALID INPUT OR FUCK OFF ......"

    levels = {
        "h": {'speed': .04, 'better food timer': 249, 'better food timer step': 15, 'best food timer step': 10,
              'best food timer': 599, },
        "m": {'speed': .08, 'better food timer': 199, 'better food timer step': 20, 'best food timer step': 15,
              'best food timer': 499, },
        "e": {'speed': .12, 'better food timer': 149, 'better food timer step': 40, 'best food timer step': 30,
              'best food timer': 399, },
    }

    timer = 0
    timer2 = 0

    SPEED = levels[level]['speed']
    BETTER_FOOD_TIMER = levels[level]['better food timer']
    BETTER_FOOD_TIMER_STEP = levels[level]['better food timer step']
    BEST_FOOD_TIMER = levels[level]['best food timer']
    BEST_FOOD_TIMER_STEP = levels[level]['best food timer step']

    screen.listen()

    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Down", fun=snake.down)

    while True:
        timer += 1
        timer2 += 1

        if snake.detect():
            board.game_over()
            break

        screen.update()
        snake.move()
        time.sleep(SPEED)

        if snake.head.distance(food) < 15:
            food.move()
            snake.grow()
            board.update()

        if timer > BETTER_FOOD_TIMER:
            better_food.showturtle()
            if snake.head.distance(better_food) < 15:
                timer = 0
                better_food.hideturtle()
                better_food.move()
                snake.grow()
                board.update(10)

        if timer == BETTER_FOOD_TIMER_STEP + BETTER_FOOD_TIMER:
            timer = 0
            better_food.hideturtle()

        if timer2 > BEST_FOOD_TIMER:
            best_food.showturtle()
            if snake.head.distance(best_food) < 15:
                timer2 = 0
                best_food.hideturtle()
                best_food.move()
                snake.grow()
                board.update(25)

        if timer2 == BEST_FOOD_TIMER_STEP + BEST_FOOD_TIMER:
            timer2 = 0
            best_food.hideturtle()
    scores.append(board.score)

try:
    game()
except:
    sys.exit()


def ask():
    message = "DO YOU WANT TO PLAY AGAIN? ENTER Y --> FOR YES OR N --> FOR NO"
    while True:
        again = screen.textinput(title="Replay?", prompt=f"{message}")
        if again is None:
            return "n"
        elif again.lower() == 'y' or again.lower() == 'n':
            return again
        else:
            message = "PLEASE ENTER A VALID INPUT OR FUCK OFF ......"

try:
    while True:
        again = ask()
        if again == "y":
            screen.reset()
            game()
        else:
            screen.bye()
            break
except:
    pass


def encrypt(string):
    string = str(string)
    encoded = ""
    for i in string:
        encoded += mapper_encode[int(i)] + " "
    return encoded


if max(scores) > maximum_score:
    score = shelve.open("score")
    score["Ran"] = encrypt(max(scores))
    score.close()

