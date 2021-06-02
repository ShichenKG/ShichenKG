import turtle             # Allows us to use turtles
import time


wn = turtle.Screen()      # Creates a playground for turtles
a = turtle.Turtle()    # Create a turtle, assign to alex
b = turtle.Turtle()    # Creates the almighty Baub the Sky God
c = turtle.Turtle()    #Creates my favorite Bob in the Bobiverse



def Spin(L,y):
    colors = ["red", "orange","yellow","green","blue","purple"]
    for x in range(50):
        color = colors[x%6]

        for l in range(10):
            a.pencolor(color)
            a.forward(L)
            a.right(31)
            a.forward(L)
            a.right(75)
            L = L+y

def Unknown():
    for r in range(3):
        b.dot(10,'green')
        b.fd(60)
        b.dot(10, 'red')
        b.bk(120)
        b.dot(10,'orange')
        b.fd(60)
        b.rt(60)
        b.dot(10,'yellow')
        for b in range(1):
            c.speed(30)
            c.circle(25,65,30)
            c.fd(20)
            c.circle(25, 65, 30)
            c.bk(40)
            c.circle(25, 65, 30)
            c.fd(20)
            c.rt(20)
            c.circle(25, 65, 30)
            for m in range(5):
                pass



a.hideturtle()
b.hideturtle()
c.hideturtle()
Spin(9,3)



wn.mainloop() 
