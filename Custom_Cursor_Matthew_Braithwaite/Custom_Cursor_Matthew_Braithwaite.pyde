# Name: Matthew Braithwaite
# Course: Computer Science 20
# Date Created: 10/02/2020
# Description: This file makes a custom cursor.


def setup():
    size(250, 250)

def draw():
    background(255)
    # Hat
    triangle(12.5, 2.0, 14.0, 5.0, 11.0, 5.0)
    # Head
    ellipse(12.5, 7.0, 5.0, 4.0)
    ellipse(11.5, 6.5, 1.0, 1.0)
    ellipse(13.5, 6.5, 1.0, 1.0)
    line(12.0, 8.0, 13.0, 8.0)
    # Body
    line(12.5, 9.0, 12.5, 16.0)
    # Legs
    line(12.5, 16.0, 9.5, 21.0)
    line(12.5, 16.0, 15.5, 21.0)
    # Arms
    line(12.5, 13.0, 7.0, 10.0)
    line(12.5, 13.0, 18.0, 14.0)
    # Cup
    line(8.0, 9.0, 6.0, 11.0)
    line(6.0, 11.0, 5.0, 10.0)
    line(5.0, 10.0, 7.0, 8.3)
    line(7.0, 8.3, 8.0, 9.0)
