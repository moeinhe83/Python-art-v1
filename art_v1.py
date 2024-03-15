# A beautiful design with Python - Part 1

# Library
from turtle import *
from colorsys import *

# Background Color & Tracer & Pensize
bgcolor('black')
tracer(5)
pensize(1.5)

# Function For Square
def square(a):
    for i in range(40):
        forward(a)
        left(100)
    forward(a)

# Value
m = 30

# Design
for i in range(15):
    color(hls_to_rgb(20, 1-i/m, 1))
    for b in range(5):
        square(5+(i*7))
# Done
hideturtle()
done()

# Create By Moein Heshmati
# Finish