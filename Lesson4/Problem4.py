from turtle import *


one = Turtle()
two = Turtle() 

one.color("blue")
one.pensize(5)
one.speed(2)
one.turtlesize(2,2,2)
one.shape("turtle")

two.color("black")
two.pensize(5)
two.speed(2)
two.turtlesize(2,2,2)
two.shape("turtle")



for x in range(3):
	one.forward(80)
	one.left(120)
	two.circle(50)

mainloop()