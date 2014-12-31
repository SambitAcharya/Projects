'''
Created For Mega Projects Repository

Turtle Graphics - This is a common project where you create a floor of 20 x 20 squares.
Using various commands you tell a turtle to draw a line on the floor. You have move forward, left or right, lift or drop pen etc.
Do a search online for "Turtle Graphics" for more information.

@author: Sambit

'''

#imports
import turtle

#Functions

#Function to draw a square
def draw_square(some_turtle):

    """

        @param Input: Turtle to perform task
        @console Output: Square pattern

    """

    for i in range(4):
        some_turtle.forward(250)
        some_turtle.right(90)

#Function to draw different shapes
def draw_art():

    """

        @param Input: None
        @console Output: Pattern

    """
    window = turtle.Screen()
    window.bgcolor("black")

    don  = turtle.Turtle()
    mike = turtle.Turtle()

    don.shape("turtle")
    don.color("purple", "green")
    don.speed(20)

    mike.shape("turtle")
    mike.color("orange", "green")
    mike.speed(20)

    for i in range(360):
        don.circle(150)
        don.right(1)

    for i in range(360):
        draw_square(mike)
        mike.right(1)

    window.exitonclick()

draw_art()
