from turtle import *
speed(13)

def sky():
    w = window_width()
    h = window_height()

    tlx = -1*w/2
    tly = h/2

    x = tlx
    y = tly
    penup()
    goto(x,y)
    pendown()
    colormode(255)
    r = 101
    #p=(101, 0, 170)
    for i in range(200):
        pencolor(r,0,170)
        #pencolor(p,0,0)
        goto(x,y)
        setheading(0)
        fd(w)
        bk(w)
        y=y-1
        r = r + 1
        if r > 255:
            r = 255
    b = 170
    for i in range(200):
        pencolor(r,0,b)
        goto(x,y)
        setheading(0)
        fd(w)
        bk(w)
        y=y-1
        r=r-1
        b=b-1
        if r < 0:
            r = 0
        if b < 0:
            b = 0
  
sky()
done()
