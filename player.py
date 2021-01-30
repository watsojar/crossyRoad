from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.color("black")
        self.goto(STARTING_POSITION)

    def upMove(self):
        newY = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), newY)

    def downMove(self):
        newY = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), newY)

    def leftMove(self):
        newX = self.xcor() - MOVE_DISTANCE
        self.goto(newX, self.ycor())

    def rightMove(self):
        newX = self.xcor() + MOVE_DISTANCE
        self.goto(newX, self.ycor())

    def playerReset(self):
        self.goto(STARTING_POSITION)
