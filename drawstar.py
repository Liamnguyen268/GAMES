#this shit is coded by Throne D. Liam (Liam Nguyen)
import turtle
import sys
window = turtle.Screen()
window.setup(600, 600)
window.bgcolor("White")
t = turtle.Turtle()
Num_Angles=int(sys.argv[1])
Num_side=int(sys.argv[2])
if Num_Angles >= 5 and Num_Angles <= 10:
 for i in range(Num_Angles):
  t.right(180/Num_Angles)
  t.forward(Num_side)
  t.right(180-(360/Num_Angles))
  t.forward(Num_side)
  t.left(180-(720/Num_Angles)+180/Num_Angles)
  #I calculate the relationship(equation) between the number of points and the angle seperate each point myself
else:
 print("Error")

window.exitonclick()

