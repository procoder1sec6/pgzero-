import pgzrun
import random
WIDTH = 410
HEIGHT = 410

def draw():
    screen.fill("#00FFFF")
    s = 200
    for i in range(40):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        screen.draw.filled_circle((205,205),s,(r,g,b))
        s = s - 5
pgzrun.go()