from turtle import *

def gradient_square(color1,color2,w=window_width(),h=window_height(),x=-window_width()/2,y=window_height()/2):
    speed(13)
    r,g,b = color1
    r2,g2,b2 = color2
    rDiff = r2 - r
    gDiff = g2 - g
    bDiff = b2 - b
    rIncr = rDiff/h
    gIncr = gDiff/h
    bIncr = bDiff/h
    penup()
    goto(x,y)
    pendown()
    colormode(255)
    for i in range(h):
        pencolor(int(r),int(g),int(b))
        fd(w)
        bk(w)
        y = y - 1
        goto(x,y)
        r = r + rIncr
        g = g + gIncr
        b = b + bIncr

gradient_square((255,0,0),(255,255,0))

done()