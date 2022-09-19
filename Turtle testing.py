from turtle import *

bgcolor('purple')
speed(-1)
# hideturtle()
for i in range(90):
    color('red')
    circle(i)
    color('pink')
    circle(i*0.8)
    right(3)
    forward(3)
done()
