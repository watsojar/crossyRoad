import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
if player.xcor() > -300 and player.xcor() < 300 and player.ycor() > -300:
    screen.onkey(player.upMove, "Up")
    screen.onkey(player.downMove, "Down")
    screen.onkey(player.leftMove, "Left")
    screen.onkey(player.rightMove, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.spawnCar()
    car.moveCars()
    scoreboard.levelText()
    scoreboard.writeHighScore()

    # Check if player completed level
    if player.ycor() > 290:
        player.playerReset()
        scoreboard.nextLevel()
        car.increaseSpeed()
      

    # Check collision with car
    for z in car.allCars:
        if player.distance(z) < 30:
            player.playerReset()
            scoreboard.resetLevel()
            car.resetSpeed()

    if scoreboard.level > scoreboard.highscore:
        scoreboard.updateHighScore()


    # check if player won
    if scoreboard.level == 15:
        game_is_on = False

scoreboard.winnerScreen()

screen.exitonclick()
