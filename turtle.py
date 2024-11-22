import turtle

fenster = turtle.Screen()
fenster.bgcolor("black")  

leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("green")
leonardo.speed(1)  

def zeichne_a():
    leonardo.pendown()
    leonardo.left(60)
    leonardo.forward(100)
    leonardo.right(120)
    leonardo.forward(100)
    leonardo.backward(50)
    leonardo.right(120)
    leonardo.forward(50)
    leonardo.penup()
    leonardo.forward(20)  

def zeichne_d():
    leonardo.pendown()
    leonardo.left(90)  
    leonardo.backward(100)
    leonardo.left(90)
    leonardo.circle(-50, 180) 
    leonardo.penup()
    leonardo.forward(20) 

def zeichne_a2():
    leonardo.pendown()
    leonardo.left(60)
    leonardo.forward(100)
    leonardo.right(120)
    leonardo.forward(100)
    leonardo.backward(50)
    leonardo.right(120)
    leonardo.forward(50)
    leonardo.penup()
    leonardo.forward(20)  

leonardo.penup()
leonardo.goto(-200, 0)  

zeichne_a()  

leonardo.goto(-30, 0) 
zeichne_d() 

leonardo.goto(90, 0)  
leonardo.left(180)
zeichne_a2() 

turtle.done()