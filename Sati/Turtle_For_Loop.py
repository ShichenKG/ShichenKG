import turtle             # Allows us to use turtles
import time


wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex
Baub = turtle.Turtle()    # Creates the almighty Baub the Sky God
Bill = turtle.Turtle()    #Creates my favorite Bob in the Bobiverse

def Square(length):
    for i in range(0,4):
        alex.forward(length)         
        alex.left(90)     

def Star():
    alex.reset()
    for i in range(1,9):
        alex.forward(100)
        alex.left(225)  

def Rose(L,y):
    colors = ["red", "hot pink", "red", "dark red"]
    for x in range(50):
        color = colors[x%4]

        for l in range(10):
            alex.pencolor(color)
            alex.forward(L)
            alex.right(31)
            alex.forward(L)
            alex.right(75)
            L = L+y

def BaubT():
    Baub.hideturtle()
    for r in range(3):
        Baub.dot(10,'green')
        Baub.fd(60)
        Baub.dot(10, 'red')
        Baub.bk(120)
        Baub.dot(10,'orange')
        Baub.fd(60)
        Baub.rt(60)
        Baub.dot(10,'yellow')
        for b in range(1):
            Bill.speed(30)
            Bill.circle(25,65,30)
            Bill.fd(20)
            Bill.circle(25, 65, 30)
            Bill.bk(40)
            Bill.circle(25, 65, 30)
            Bill.fd(20)
            Bill.rt(20)
            Bill.circle(25, 65, 30)
            for m in range(5):
                pass



BaubT()
Rose(9,3)
time.sleep(1)
Square(40)
time.sleep(1)
Star()


wn.mainloop() 
