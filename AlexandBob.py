import turtle

# create Alex the Turtle
Alex = turtle.Turtle()
Alex.shape('turtle')

# make Alex do a colorful square
for c in ['red', 'green', 'yellow', 'blue', 'purple', 'turquoise']:
    Alex.pencolor(c)
    Alex.forward(75)
    Alex.left(90)
    


# create Bob the turtle
Bob = turtle.Turtle()
Bob.shape('turtle')
Bob.penup()
Bob.setposition(100, 40)
Bob.pencolor('blue')
Bob.pendown()

# make Bob draw a star, and keep doing it forever
while True:
    Bob.forward(75)
    Bob.left(190)
