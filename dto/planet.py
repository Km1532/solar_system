from typing import NamedTuple, Tuple, Union
import turtle
import random

class PlanetData(NamedTuple):
    planet_size: Tuple[float, float]
    planet_color: Union[str, Tuple[float, float, float]]
    radius: int
    increase_angle: float
    name: str = 'star'

def starFILL(n, dlina):
    joe.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            joe.forward(dlina)
            angle = n // 2 * 360 / n
            joe.left(angle)
    joe.end_fill()

window = turtle.Screen()
window.bgcolor('black')

for i in range(20):
    joe = turtle.Turtle()
    joe.color('yellow')
    joe.speed(20)
    x = random.randint(-320, 320)
    y = random.randint(-220, 320)
    joe.up()
    joe.setposition(x, y)
    joe.down()
    size = random.randint(10, 20)
    starFILL(5, size)
