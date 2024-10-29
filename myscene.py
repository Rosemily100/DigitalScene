from turtle import *
from random import randrange

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
    g=128
    for i in range(265):
        pencolor(0,g,0)
        goto(x,y)
        setheading(0)
        fd(w)
        bk(w)
        y=y-1
        r=r-1
        b=b-1
        if r < 0:
            r = 0
        if g < 0:
            g = 0
  


def draw_shape(side_length,num_sides):
    penup()
    pendown()
    colormode(255)
    width(1)
    pencolor(0,255,0)
    angle = 360/num_sides
    fillcolor(0,255,0)
    begin_fill()
    for i in range(num_sides):
        fd(side_length)
        left(angle)
    end_fill()
    penup()

def draw_tree(x,y,side_length,num_tri):
    penup()
    for i in range(num_tri):
        goto(x,y)
        draw_shape(side_length,3)
        lastX = x
        lastY = y
        last_side_length = side_length
        x = x - side_length/3
        y = y - side_length
        side_length = side_length + side_length/1.5
    goto(lastX + (last_side_length/5)*2,lastY)
    fillcolor("brown")
    begin_fill()
    forward(last_side_length/5)
    rt(90)
    forward(last_side_length/3)
    rt(90)    
    forward(last_side_length/5)
    rt(90)
    forward(last_side_length/3)
    rt(90)
    end_fill()


def draw_forest():
    num_trees = 20
    w = window_width()
    h = window_height()
    for i in range(num_trees):
        x = randrange(-400,400)
        y = randrange(-400,0)
        l = randrange(5,15)
        t = randrange(2,5)
        draw_tree(x,y,l,t)

def star():
    pendown()
    for i in range(8):
        l =randrange(10,40)
        fd(l)
        bk(l)
        rt(45)
    penup()

def stars(num):
    pencolor("white")
    for i in range(num):
        penup()
        goto(randrange(-500,500),randrange(0,400))
        star()



speed(13)
sky()
stars(20)
#draw_forest()
    
    
done()

