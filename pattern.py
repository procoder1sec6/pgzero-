import pgzrun
import random
WIDTH = 410
HEIGHT = 410
def draw():
    screen.fill("#00FFFF")
    w = 410
    h = 170
    for i in range(26 * 5):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        t = Rect((205,205),(w,h))
        t.center = 205,205
        screen.draw.rect(t,(r,g,b))
        w = w - 10 / 5
        h = h + 10 / 5
pgzrun.go()