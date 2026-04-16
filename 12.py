import turtle

turtle.speed(5)
turtle.width(2)


def draw_square():
    turtle.color("crimson")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(40)
        turtle.right(90)
    turtle.end_fill()


def draw_circle():
    turtle.color("royalblue")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


def draw_triangle():
    turtle.color("gold")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(40)
        turtle.left(120)
    turtle.end_fill()


turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()

for _ in range(4):
    draw_square()
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

    draw_circle()
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

    draw_triangle()
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

turtle.hideturtle()
turtle.done()
