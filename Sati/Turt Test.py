import turtle
import time

window = turtle.Screen()
t = turtle.Turtle()



t.penup()
t.sety(-150)
t.pendown()
t.speed(20)
t.hideturtle()
def fcircle():
    colors = ["red","orange","yellow","green","#04d69e","blue","purple","indigo",""]
    num = [130,120,110,100,90,80,70,60,50,60,70,80,90,100,110,120,130]
    pos = [-350,-300,-250,-200,-150,-100,-50,0,50,100,150,200,250,300,
           250,200,150,100,50,0,-50,-100,-150,-200,-250,-300,-350]
    
    for x in range(1000):
        color = colors[x%8]
        numbers = num[x%17]
        position = pos[x%27]
        
        
        for c in range(1):
            t.pencolor(color)
            t.pensize(numbers)
            t.circle(150)
            t.sety(position)

def donut():
    colors = ["#126b06","#147507","#157a07","#167d07","#188708","#198f09",
              "#199409","#1a9909","#1ba10a","#1ca80a","#1dad0a","#1eb30b",
              "#1fba0b","#21bd0d","#23c70e",
              "#24cf0e",
              "#23c70e","#23c70e","#1fba0b",
              "#1fba0b","#1dad0a","#1ca80a","#1ba10a","#1a9909","#199409",
              "#198f09","#188708","#167d07","#157a07","#147507","#126b06"]
    num = [320,300,280,260,240,220,200,180,160,140,120,100,80,60,40,
           20,
           40,60,80,100,120,140,160,180,200,220,240,260,280,300,320]
    pos = [-150]
    
    for x in range(60):
        color = colors[x%30]
        numbers = num[x%30]
        position = pos[x%1]
        
        
        for c in range(1):
            t.pencolor(color)
            t.pensize(numbers)
            t.circle(150)
            t.sety(position)

dad = 1000
birth = donut()
regret = t.clear()
smash = range

for yourmom in smash(1000):
    donut()
    t.clear()

