import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

drawer = turtle.Turtle()
drawer.color("white")
drawer.speed(0)

def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)

for _ in range(32):
    draw_square(drawer, 100)
    drawer.right(360 / 32)

turtle.done()
