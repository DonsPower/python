import turtle

painter = turtle.Turtle()

painter.pencolor("blue")
painter.speed(15)
for i in range(50):
    painter.forward(50)
    painter.left(123)
painter.setposition(0, 0)
painter.pendown()

painter.pencolor("red")

for i in range(50):
    painter.forward(100)
    painter.left(123)
    painter.right(30)
painter.setposition(-100, -100)
painter.speed(25)
painter.pencolor("green")
for i in range(180):
    painter.forward(100)
    painter.right(30)
    painter.forward(20)
    painter.left(60)
    painter.forward(50)
    painter.right(30)
    painter.penup()
    painter.setposition(-100, -100)
    painter.pendown()

    painter.right(2)
painter.setposition(100, 100)
painter.speed(25)
painter.pencolor("black")
for i in range(180):
    painter.forward(100)
    painter.right(30)
    painter.forward(20)
    painter.left(60)
    painter.forward(50)
    painter.right(30)
    painter.penup()
    painter.setposition(100, 100)
    painter.pendown()

    painter.right(2)
painter.setposition(-200, -200)
painter.speed(25)
painter.pencolor("purple")
for i in range(180):
    painter.forward(100)
    painter.right(30)
    painter.forward(20)
    painter.left(60)
    painter.forward(50)
    painter.right(30)
    painter.penup()
    painter.setposition(-200, -200)
    painter.pendown()

    painter.right(2)
painter.setposition(200, 200)
painter.speed(25)
painter.pencolor("pink")
for i in range(180):
    painter.forward(100)
    painter.right(30)
    painter.forward(20)
    painter.left(60)
    painter.forward(50)
    painter.right(30)
    painter.penup()
    painter.setposition(200, 200)
    painter.pendown()

    painter.right(2)

turtle.done()
