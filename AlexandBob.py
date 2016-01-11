import turtle

inputDegrees = input('How many degrees should Alex turn (0-360)?')

degrees = int(inputDegrees)


def turtleSquare(thisTurtle):
    
    for c in ['red', 'green', 'yellow', 'blue', 'purple']:
        thisTurtle.pencolor(c)
        thisTurtle.forward(75)
        thisTurtle.left(degrees)


def turtleStar(thisTurtle):
    for i in range(18):
        Bob.forward(75)
        Bob.left(190)


# create Alex the Turtle
Alex = turtle.Turtle()
Alex.shape('turtle')

  
# create Bob the turtle
Bob = turtle.Turtle()
Bob.shape('turtle')
Bob.penup()
Bob.setposition(100, 40)
Bob.pencolor('blue')
Bob.pendown()


turtleSquare(Alex)
turtleStar(Bob)



