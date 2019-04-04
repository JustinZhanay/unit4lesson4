from turtle import*

Squirtle = Turtle ()

Squirtle.color('Blue')
Squirtle.pensize(5)
Squirtle.speed(9)
Squirtle.shape('turtle')

#DRAWING INSTRUCTIONS
for y in range(1):

	#original shape
	Squirtle.forward(80)
	Squirtle.left(50)
	Squirtle.forward(200)
	Squirtle.right(150)
	Squirtle.forward(50)
	Squirtle.circle(25)
	Squirtle.backward(30)
	Squirtle.circle(50)



mainloop()