from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):

    def __init__(self):
        super(CarManager, self).__init__()
        self.allCars = []
        self.hideturtle()
        self.moveDistance = 5

    def moveCars(self):
        for car in self.allCars:
            car.backward(self.moveDistance)

    def spawnCar(self):
        randomChance = random.randint(1, 6)
        if randomChance == 1:
            newCar = Turtle("square")
            newCar.penup()
            newCar.shapesize(stretch_len=2, stretch_wid=1)
            newCar.color(random.choice(COLORS))
            yCor = random.randint(-250, 250)
            newCar.goto(300, yCor)
            self.allCars.append(newCar)

    def increaseSpeed(self):
        self.moveDistance += 1
        print(self.moveDistance)

    def resetSpeed(self):
        self.moveDistance = 5


