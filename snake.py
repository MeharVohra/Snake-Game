import turtle

# positions of the three squares
positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # All three squares would be in on top of each other
        # if we don't provide their coordinates.
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        # Here, we added 2 more segments to the first one on different coordinates.
        # Each segment is 20 by 20. So the first one will be at (0,0), the 2nd one
        # will be at (-20, 0) and the 3rd one will be at tge coordinates (-40,0).

        choco = turtle.Turtle(shape="square")
        choco.color("green")
        choco.speed(1)
        # if we don't use penup(), a line will also be drawn while positioning the segments.
        choco.penup()
        choco.goto(position)
        self.segments.append(choco)

    def increase_length_of_snake(self):
        # Every time the snake will eat the food and the score will increase by one,
        # the length of the snake will also keep increasing by one segment.
        # This segment will append at the end of the segment.
        self.add_segment(self.segments[-1].position())

    def move(self):
        # There are 3 segments so the 3rd one will move to where the 2nd segment is,
        # 2nd will move to where the 1st segment is the 1st segment which is the head will move
        # in the specified direction
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)

        # This is the head of the snake i.e the first segment
        self.head.forward(20)

    def reset(self):
        # Even after the segments are cleared and the new snake is created,
        # the previous snake is still visible. So, in order for the snake to
        # be invisible, we will send it to a position which is off the screen.
        # That's why we have set the coordinates to (1000,1000)
        for seg in self.segments:
            seg.goto(1000, 1000)
        # All the segments added to the list will be deleted
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        # with the help of this statement, when the head is down,
        # we cannot move it upwards. If the head is not down, only then
        # we can move it upwards.
        if self.head.heading() != DOWN:
            # We set the heading to upwards = 90
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
