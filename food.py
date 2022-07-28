from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Create the food of the snake in the shape of a circle
        self.shape("circle")
        self.color("red")
        self.penup()
        # Normally the size of the circle is 20 by 20, but
        # with the help of shapesize method we have reduced it to
        # 10 by 10
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def refresh(self):
        # as soon as the snake will collide with snake, the food
        # will move to another random location
        random_x = random.randint(-250, 180)
        random_y = random.randint(-250, 180)
        self.goto(random_x, random_y)


