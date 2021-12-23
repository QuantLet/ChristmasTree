import logging
import os
import turtle
import random

from gif_creator import GIFCreator, init

init()

def draw_circle_image(image, size, x, y):
    fullname = "{image}-{size}.gif".format(image=image, size=size)
    full_path = os.path.join("pics", fullname)
    ttl = turtle.Turtle(full_path)
    ttl.penup()
    ttl.goto(x, y)
    ttl.shape(full_path)
    ttl.resizemode("auto")
    ttl.pendown()

# method 2: use class
# If you want to create a class, just define your draw function, and then record it.
class ChristmasTree(GIFCreator):
    DURATION = 200  # optional

    def draw(self):
        bg = turtle.Screen()
        bg.bgcolor("white")

        for filename in os.listdir("pics"):
            if not filename.startswith('.'):
                full_path = os.path.join("pics", filename)
                logging.info(full_path)
                bg.addshape(full_path)

        ornament_list = ["quantinar", "quantlet"]
        size_list = ["15x15", "20x20", "25x25", "30x30"]

        tina = turtle.Turtle()
        tina.shape("turtle")
        tina.speed(10)

        tina.penup()
        tina.goto(0, 0)
        tina.color("green")
        tina.begin_fill()
        tina.fillcolor("green")
        tina.pensize(8)
        tina.pendown()
        tina.goto(100, 0)
        tina.penup()
        tina.end_fill()

        tina.goto(100, 0)
        tina.pendown()
        tina.color("green")
        tina.begin_fill()
        tina.fillcolor("green")
        tina.goto(0, 75)
        tina.goto(-100, 0)
        tina.forward(100)
        tina.goto(125, -65)
        tina.goto(-125, -65)
        tina.goto(0, 0)
        tina.penup()
        tina.end_fill()

        tina.goto(0, 75)
        tina.pendown()
        tina.color("green")
        tina.begin_fill()
        tina.fillcolor("green")
        tina.goto(50, 75)
        tina.goto(0, 120)
        tina.goto(-50, 75)
        tina.goto(0, 75)
        tina.penup()
        tina.end_fill()

        tina.goto(0, -90)
        tina.pendown()
        tina.color("brown")
        tina.begin_fill()
        tina.fillcolor("brown")
        tina.goto(20, -90)
        tina.left(90)
        tina.forward(20)
        tina.left(90)
        tina.forward(40)
        tina.left(90)
        tina.forward(20)
        tina.left(90)
        tina.forward(20)
        tina.penup()
        tina.end_fill()

        for i in range(18):
            tina.penup()
            x = random.randint(-75, 75)
            y = random.randint(-65, 120)
            size = (random.choice(size_list))
            image = (random.choice(ornament_list))
            tina.goto(x, y)
            tina.pendown()
            draw_circle_image(image, size, x, y)
            tina.penup()

            tina.goto(250, -250)
            turtle.hideturtle()

        turtle.exitonclick()

ChristmasTree(name='christmas').record()
