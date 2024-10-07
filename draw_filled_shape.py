from turtle import *

def draw_shape(side_length,num_sides):
    penup()
    goto(-200,200)
    pendown()
    colormode(255)
    width(5)
    pencolor(255,0,0)
    angle = 360/num_sides
    fillcolor(255,0,255)
    begin_fill()
    for i in range(num_sides):
        fd(side_length)
        right(angle)
    end_fill()


draw_shape(150,8)

done()