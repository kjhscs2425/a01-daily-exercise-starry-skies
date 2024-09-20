
import turtle
numberofsides = 3


def draw():
         for i in range (3):
                turtle.forward(100)
                turtle.left(360/numberofsides)
for i in range(3):
        draw()
        turtle.right(120)
turtle.right(60)
for i in range(3):
       draw()
       turtle.right(120)
        

    

     
    

turtle.exitonclick()

