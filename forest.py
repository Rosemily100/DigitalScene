from turtle import *
from random import randrange

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
    for i in range(num_trees):
        x = randrange(-400,400)
        y = randrange(-350,350)
        l = randrange(10,30)
        t = randrange(2,5)
        draw_tree(x,y,l,t)

speed(13)
draw_forest()

done()
