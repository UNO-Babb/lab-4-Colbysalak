#TurtleGraphics.py
#Name: Colby Salak
#Date:9/22/24
#Assignment: TurtleGraphics.py

import turtle #needed generally but not in CodeHS 
size = input ("How long should the sides of the polygon be: ")
sides = input("How many sides for the polygon: ")

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
sides = int(sides)
size = int(size)

angle=360 / sides
def drawPolygon(myTurtle, sides):
    myTurtle.up()
    myTurtle.goto(25,-25)
    myTurtle.down()


def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

corner = input("When fillinga corner of a square, choose the 1,2,3, or 4 corner: ")

corner=int(corner)
size2 = size / 2
def fillCorner (myTurtle, corner):
    myTurtle.up()
    myTurtle.goto(-size2,size2)
    myTurtle.down()

    drawSquare(myTurtle, size)

    if corner== 1:
        myTurtle.position()
    if corner== 2:
        myTurtle.forward(size2)
    
    if corner== 3:
        myTurtle.right(90)
        myTurtle.forward(size2)
        myTurtle.left(90)
    
    if corner== 4:
        myTurtle.forward(size)
        myTurtle.right(90)
        myTurtle.forward(size2)

    myTurtle.begin.fill()
    drawSquare(myTurtle, size2)
    myTurtle.end_fill()

num = input("When stacking squares, how many squares should be stacked together: ")

num = int(num)
def squaresInSquares(myTurtle, num):

    size3= 10
    myTurtle.up()
    myTurtle.goto(-size3/2, size3/2)
    myTurtle.down()

    for i in range(num):
        drawSquare(myTurtle, size3)
        size3 = size3 + 10

        myTurtle.up()
        myTurtle.goto(-size3/2, size3/2)
        myTurtle.down()

def main():
    myTurtle = turtle.Turtle()
    drawPolygon(myTurtle)
    #fillCorner(myTurtle, corner)
    #sqauresInSquares (myTurtle, num)
    # drawPolygon(myTurtle, 5) #draws a pentagon
    drawPolygon(myTurtle, 8) #draws an octogon

    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
input("Hit enter to quit")
