import pgzrun
WIDTH = 410
HEIGHT = 410
def draw():
    screen.fill("light blue")
    r = Rect((660,380),(30,30))
    screen.draw.filled_rect(r,"black")
    screen.draw.filled_circle((205,205),200,"#FFFF00")
    screen.draw.filled_circle((140,130),30,"#000000")
    screen.draw.filled_circle((270,130),30,"#000000")
    screen.draw.filled_circle((205,250),70,"#000000")
    screen.draw.filled_circle((205,250),40,"#FFFF00")
    p = Rect((205,205),(150,83))
    p.center = 205,221
    screen.draw.filled_rect(p,"#FFFF00")
pgzrun.go()