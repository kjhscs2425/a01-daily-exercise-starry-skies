
import turtle
numberofsides = 3


def draw():
         for i in range (3):
                turtle.forward(100)
                turtle.left(360/numberofsides)
for i in range(3):
        draw()
        turtle.right(120)
turtle.left(180)
draw()
for i in range (2):
       turtle.right(120)
       draw()
    

     
    

turtle.exitonclick()

