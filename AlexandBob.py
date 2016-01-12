import turtle


# ask the user for their choice of turtle turn 
inputDegrees = raw_input('How many degrees should Alex turn (0-360)?')
# convert the choice (a string) into a number (an int)
degrees = int(inputDegrees)

# these are the two functions that describe what we want the turtles to do. They take one argument, which is the turtle of choice.
def turtleSquare(thisTurtle):
    
    for c in ['red', 'green', 'yellow', 'blue', 'purple']:
        thisTurtle.pencolor(c)
        thisTurtle.forward(75)
        thisTurtle.left(degrees)

def turtleStar(thisTurtle):
    for i in range(36):
        thisTurtle.forward(75)
        thisTurtle.left(190)

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

userWait = raw_input('We did not make the turtles do anything yet. Time to call the functions and pass the turtles! Press Ok or Enter to continue')

turtleSquare(Alex)
turtleStar(Bob)
turtleStar(Alex)        # now Alex doesn't feel left out. He's a star too...

