import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

BACKGROUND_COLORS = ['#B5CF49', '#A3BF45', '#81A140', '#74923A', '#617B30']
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor(BACKGROUND_COLORS[0])

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
if -300 < player.xcor() < 300 and player.ycor() > -300:
    screen.onkey(player.upMove, "Up")
    screen.onkey(player.downMove, "Down")
    screen.onkey(player.leftMove, "Left")
    screen.onkey(player.rightMove, "Right")

gameRun = False


def gameRunTrue(x, y):
    global gameRun
    gameRun = True
    scoreboard.clear()


def startGame():
    global gameRun
    while not gameRun:
        scoreboard.startScreen()
        screen.onscreenclick(gameRunTrue, 1)


startGame()
while gameRun:
    time.sleep(0.1)
    screen.update()
    car.spawnCar(scoreboard.level)
    car.moveCars()
    scoreboard.levelText()
    scoreboard.writeHighScore()

    # Check if player completed level
    if player.ycor() > 290:
        scoreboard.levelComplete()
        scoreboard.nextLevel()
        player.playerReset()
        scoreboard.nextLevel()
        car.increaseSpeed()

    # Check collision with car
    for z in car.allCars:
        if player.distance(z) < 30:
            scoreboard.gameOver()
            player.playerReset()
            scoreboard.resetLevel()
            car.resetSpeed()

    if scoreboard.level > scoreboard.highscore:
        scoreboard.updateHighScore()

    # make background darker each level
    try:
        screen.bgcolor(BACKGROUND_COLORS[scoreboard.level - 1])
    except IndexError:
        screen.bgcolor(BACKGROUND_COLORS[len(BACKGROUND_COLORS) - 1])

    # check if player won
    if scoreboard.level == 15:
        gameRun = False

scoreboard.winnerScreen()

screen.exitonclick()
