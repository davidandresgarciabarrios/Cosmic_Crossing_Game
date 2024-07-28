from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class AsteroidManager:
    def __init__(self):
        self.all_asteroids = []
        self.asteroid_speed = STARTING_MOVE_DISTANCE

    def create_asteroid(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_asteroid = Turtle("asteroid")
            new_asteroid.shapesize(1, 1)
            new_asteroid.penup()
            new_asteroid.color("white")
            random_y = random.randint(-180, 180)
            new_asteroid.goto(300, random_y)
            self.all_asteroids.append(new_asteroid)

    def move_asteroids(self):
        for asteroid in self.all_asteroids:
            asteroid.backward(self.asteroid_speed)

    def level_up(self):
        self.asteroid_speed += MOVE_INCREMENT
