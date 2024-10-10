from turtle import *
from random import randrange

def draw_shape(side_length,num_sides):
    setheading(0)
    penup()
    pendown()
    colormode(255)
    width(2)
    green = 255
    incr = 255/side_length
    num = int(side_length)
    for i in range(num):
        pencolor(0,int(green),0)
        for i in range(3):
            fd(side_length)
            lt(120)
        green = green - incr
        side_length = side_length - 1
    penup()


def draw_tree(x,y,side_length,num_tri):
    penup()
    firstX = x
    firstY = y
    first_side_length = side_length
    for i in range(num_tri):
        goto(x,y)
        draw_shape(side_length,3)

        x = x + side_length/6
        y = y + (side_length/1.5)
        side_length = side_length - (side_length/3)
    goto(firstX + (first_side_length/5)*2,firstY)
    fillcolor("brown")
    begin_fill()
    forward(first_side_length/5)
    rt(90)
    forward(first_side_length/3)
    rt(90)    
    forward(first_side_length/5)
    rt(90)
    forward(first_side_length/3)
    rt(90)
    end_fill()

def draw_sun():
    penup()
    goto(window_width()/2,window_height()/2)
    colormode(255)
    h = 180
    pendown()
    for i in range(90):
        pencolor(255,randrange(150,255),randrange(0,100))
        width(randrange(4,8))
        setheading(h)
        d = randrange(150,300)
        fd(d)
        bk(d)
        h = h+1
    penup()
    pencolor(255,255,0)
    dot(150)

def draw_moon(size):
    penup()
    goto(window_width()/2 - 150,window_height()/2 - 150)
    colormode(255)
    grey = 230
    pencolor(grey,grey,grey)
    dot(size)
    h = 0
    for i in range(18):
        grey = randrange(190,215)
        pencolor(grey,grey,grey)
        setheading(h)
        d = randrange(20,int(size/2 - 20))
        fd(d)
        dot(randrange(10,20))
        bk(d)
        h = h + 20


def draw_simple_shape(side_length,num_sides):
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

def draw_simple_tree(x,y,side_length,num_tri):
    penup()
    for i in range(num_tri):
        goto(x,y)
        draw_simple_shape(side_length,3)
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


def draw_simple_forest():
    num_trees = 20
    setheading(0)
    for i in range(num_trees):
        x = randrange(-400,400)
        y = randrange(-350,350)
        l = randrange(10,30)
        t = randrange(2,5)
        draw_simple_tree(x,y,l,t)


def draw_stars(num_stars):
    penup()
    pencolor("white")
    for i in range(num_stars):
        x = randrange(int(-window_width()/2),int(window_width()/2))
        y = randrange(int(window_height()/4),int(window_height()/2))
        goto(x,y)
        pendown()
        for i in range(4):
            d = randrange(2,10)
            fd(d)
            bk(d)
            rt(45)
            fd(d/2)
            bk(d/2)
            rt(45)
        penup()

def draw_birds(num_birds):
    penup()
    pencolor("black")
    for i in range(num_birds):
        size=randrange(4,20)
        setheading(100)
        x = randrange(int(-window_width()/2),int(window_width()/2))
        y = randrange(int(window_height()/4),404)
        goto(x,y)
        pendown()
        width(3)
        circle(size,175)
        rt(180)
        circle(size,175)
        penup()

def lake():
    pass

def draw_forest(num_trees,day = True):
    if day:
        bgcolor(135, 206, 235)
        draw_sun()
        draw_birds(7)
    else:
        bgcolor(10, 10, 97)
        draw_stars(40)
        draw_moon(200)
    draw_simple_forest()
    for i in range(num_trees):
        x = randrange(-450,400)
        y = randrange(-375,0)
        l = randrange(40,80)
        t = randrange(2,4)
        draw_tree(x,y,l,t)

def window_dimensions():
    # these are the dimensions
    h = window_height()
    w = window_width()
    
    tlX = w/2*-1
    tlY = h/2
    penup()
    goto(100,100)
    write("Maximize this window to see coordinates!")
    goto(tlX,tlY)
    pendown()
    write(pos())
    trX = tlX * -1
    trY = tlY
    goto(trX,trY)
    write(pos())
    brX = trX
    brY = trY * -1
    goto(brX,brY)
    write(pos())
    blX = tlX
    blY = tlY * -1
    goto(blX,blY)
    write(pos())
    goto(tlX,tlY)
    goto(w/2*-1,0)
    write(pos())
    goto(w/2,0)
    write(f"({w/2},0)")
    penup()
    goto(0,h/2*-1)
    write(pos())
    pendown()
    goto(0,h/2)
    write(pos())
    penup()
    goto(0,0)
    write(pos())


WIDTH, HEIGHT = 1000, 800
screen = Screen()
screen.setup(WIDTH, HEIGHT) 
speed(13)
hideturtle()
colormode(255)
draw_forest(3)


window_dimensions()
done()
