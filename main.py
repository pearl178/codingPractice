from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
screen = Screen()


def draw_square():
    for _ in range(4): # run 4 times
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)


def draw_dotted_line():
    for _ in range(10):
        timmy_the_turtle.pd()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pu()
        timmy_the_turtle.forward(10)


def draw_different_shapes():
    n=3
    while n < 10:
        screen.colormode(255)
        timmy_the_turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        t = 0
        angle = 360/n
        while t < n:
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(angle)
            t += 1
        n += 1


def random_walk():
    def choose_direction():
        angels = [0, 90, 180, 270]
        return random.choice(angels)
    timmy_the_turtle.pensize(10)
    timmy_the_turtle.speed(10)
    for _ in range(100):
        screen.colormode(255)
        timmy_the_turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        timmy_the_turtle.right(choose_direction())
        timmy_the_turtle.forward(20)


def draw_spirograph():
    timmy_the_turtle.speed("fastest")
    for _ in range(int(360/5)):
        screen.colormode(255)
        timmy_the_turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        timmy_the_turtle.circle(100)
        timmy_the_turtle.right(5)


draw_spirograph()

screen.exitonclick()