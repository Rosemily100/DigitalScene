from turtle import *

def window_dimensions():

    WIDTH, HEIGHT = 1000, 800
    screen = Screen()
    screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar

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

speed(13)
window_dimensions()

done()

