import pgzrun
WIDTH = 690
HEIGHT = 410
def draw():
    screen.fill("light blue")
    r = Rect((330,190),(30,30))
    l = Rect((660,0),(30,60))
    r.center = 345,205
    screen.draw.rect(r,"black")
    screen.draw.filled_rect(l,"black")
pgzrun.go()