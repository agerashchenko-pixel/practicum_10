import turtle


turtle.speed(5)
turtle.width(2)


def draw_square():
    """
    Draw a square filled with crimson color.
    :return: None
    """
    turtle.color("crimson")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(40)
        turtle.right(90)
    turtle.end_fill()


def draw_circle():
    """
    Draw a circle filled with royalblue color.
    :return: None
    """
    turtle.color("royalblue")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


def draw_triangle():
    """
    Draw an equilateral triangle filled with gold color.
    :return: None
    """
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
