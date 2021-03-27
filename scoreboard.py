from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        with open("data.txt") as data:
            self.highscore = int(data.read())

    def startScreen(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("Click to Start!", align="center", font=("Courier", 60, "normal"))

    def nextLevel(self):
        self.clear()
        self.level += 1

    def resetLevel(self):
        self.clear()
        self.level = 1

    def levelText(self):
        self.goto(-280, 260)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def winnerScreen(self):
        self.clear()
        self.goto(0, -20)
        self.write("You win!", align="center", font=("Courier", 100, "normal"))

    def updateHighScore(self):
        self.clear()
        if self.level > self.highscore:
            self.highscore = self.level
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")

    def writeHighScore(self):
        self.goto(180, 260)
        self.write(f"Highscore: {self.highscore}", align="center", font=FONT)

    def levelComplete(self):
        text = Turtle()
        text.penup()
        text.hideturtle()
        text.goto(0, -20)
        text.color('#8E44AD')
        text.write(f"Level {self.level + 1}", align="center", font=("Courier", 75, "normal"))
        time.sleep(1)
        self.level -= 1
        text.clear()

    def gameOver(self):
        text = Turtle()
        text.penup()
        text.hideturtle()
        text.goto(0, -20)
        text.color("red")

        text.write("GAME OVER", align="center", font=("Courier", 75, "normal"))
        time.sleep(3)
        text.clear()


