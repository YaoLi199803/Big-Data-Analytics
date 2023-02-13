import turtle 
import time 
import math

# Draw the hour, minute and second hands on the colck
size=150
t=turtle.Pen()
t_s=turtle.Pen()
t_s.pensize(size*0.01)
t_s.resizemode("auto")
t_m=turtle.Pen()
t_m.pensize(size*0.02)
t_m.resizemode("auto")
t_h=turtle.Pen()
t_h.pensize(size*0.04)
t_h.resizemode("auto")

t.ht()


# Draw the colck
def bg_watch():
    turtle.tracer(False)     
    t.up()
    t.goto(0,size)
    t.down()
    for i in range(12):
        x,y=t.pos()
        heading=t.heading()

        t.right(90)
        t.forward(size*0.1)
        
        t.up()
        t.forward(size*0.1)
        t.seth(0)
        t.down()
        if i==0:
            t.write(12)
        else:
            t.write(i)
        t.up()
        t.goto(x,y)
        t.seth(heading)
        t.down()
        t.circle(-size,360/12)
    turtle.tracer(True)


# get the time of the clock
def sec2ag():
    turtle.tracer(False)
    a=time.time()
    t_s.home()
    t_s.clear()
    sec_now=time.localtime()[5]
    t_s.seth(-(sec_now*6-90))
    t_s.forward(size*0.7)
    turtle.tracer(True)
    b=time.time()
    while b-a<1:
        b=time.time()


def min2ag():
    turtle.tracer(False)
    t_m.home()
    t_m.clear()
    min_now=time.localtime()[4]
    sec_now=time.localtime()[5]
    t_m.seth(-(min_now*6-90)-sec_now/60*6)
    t_m.forward(size*0.5)
    turtle.tracer(True)


def h2ag():
    turtle.tracer(False)
    t_h.home()
    t_h.clear()
    hour_now=time.localtime()[3]
    min_now=time.localtime()[4]
    t_h.seth(-(hour_now%12*30-90)-min_now/60*30)
    t_h.forward(size*0.3)
    turtle.tracer(True)
   

bg_watch()

# call the define function
while True:
    h2ag()
    min2ag()
    sec2ag()
 