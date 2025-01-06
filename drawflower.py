# @liamthrone/ my instagram
import turtle
import sys
window = turtle.Screen()
window.setup(600, 600)
window.bgcolor("White")
t = turtle.Turtle()
num_squares = int(sys.argv[1])
side_length = int(sys.argv[2])
for i in range(num_squares):
    for i in range(4):
      t.forward(side_length)
      t.right(90)
    t.right(90+((360-(90*num_squares))/num_squares))
 
window.exitonclick()