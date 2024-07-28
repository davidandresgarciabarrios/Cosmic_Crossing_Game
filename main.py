import time
from turtle import Screen, Shape
from player import Player
from asteroid_manager import AsteroidManager
from scoreboard import Scoreboard

# Create a screen instance
screen = Screen()
screen.bgcolor("black")

# Define the rocket shape
rocket_shape = [
    (0, 20), (-5, 10), (-5, 0), (-15, -10), (0, -20),
    (15, -10), (5, 0), (5, 10), (0, 20)
]

# Define the asteroid shape
asteroid_shape = [
    (0, 20), (-6, 16), (-14, 10), (-18, 0), (-14, -10),
    (-6, -16), (0, -20), (6, -16), (14, -10), (18, 0),
    (14, 10), (6, 16), (0, 20)
]

# Convert shapes to turtle Shape format
rocket = Shape("polygon", rocket_shape)
asteroid = Shape("polygon", asteroid_shape)

# Register the shapes
screen.register_shape("rocket", rocket)
screen.register_shape("asteroid", asteroid)

screen.setup(width=600, height=600)
screen.title("Cosmic Crossing")
screen.tracer(0)

player = Player()
asteroid_manager = AsteroidManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    asteroid_manager.create_asteroid()
    asteroid_manager.move_asteroids()

    # Detecting collision with car:
    for car in asteroid_manager.all_asteroids:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Detecting successful crossing:
    if player.is_at_finish_line():
        player.go_to_start()
        asteroid_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
