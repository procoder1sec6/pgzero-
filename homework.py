import pgzrun
WIDTH = 690
HEIGHT = 410
def draw():
    screen.fill("light blue")
    l = Rect((0,0),(30,30))
    r = Rect((660,380),(30,30))
    screen.draw.filled_rect(r,"black")
    screen.draw.filled_rect(l,"black")
    t = Rect((0,380),(30,30))
    p = Rect((660,0),(30,30))
    screen.draw.rect(t,"black")
    screen.draw.rect(p,"black")
pgzrun.go()