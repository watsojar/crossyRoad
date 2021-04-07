from turtle import Turtle
import random
image = "car1.png"

COLORS = [["#d11141", "#00b159", "#00aedb", "#f37735", "#ffc425"],
          ["#0b9f9f", "#059898", "#059090", '#028989', "#027e7e"],
          ["#c1faff", "#b2eaff", "#a2c9ff", "#d2afff", "#d496ff"]]


class CarManager(Turtle):

    def __init__(self):
        super(CarManager, self).__init__()
        self.allCars = []
        self.hideturtle()
        self.moveDistance = 5
        self.colorPicker = 0

    def moveCars(self):
        for car in self.allCars:
            car.backward(self.moveDistance)

    def spawnCar(self, level):
        randomChance = random.randint(1, 6)
        if randomChance == 1:
            newCar = Turtle("square")
            newCar.penup()
            newCar.shapesize(stretch_len=2, stretch_wid=1)
            if level % 3 == 0:
                newCar.color(random.choice(COLORS[0]))
            if level % 2 == 0:
                newCar.color(random.choice(COLORS[1]))
            else:
                newCar.color(random.choice(COLORS[2]))
            yCor = random.randint(-250, 250)
            newCar.goto(300, yCor)
            self.allCars.append(newCar)

    def increaseSpeed(self):
        self.moveDistance += 1

    def resetSpeed(self):
        self.moveDistance = 5
