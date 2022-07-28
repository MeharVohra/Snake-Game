from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

# Setup of the screen
# The screen is 600 by 600
screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("My Snake Game")

# The 3 segments will move forward or in the specified direction individually.
# But we want it to move as a whole, so we used tracer to turn that animation off.
screen.tracer(0)

snake = Snake()

# listen() method is called for listening to the keystrokes
# i.e the keyboard arrows up, down, right and left.
screen.listen()
food = Food()
food.refresh()
score = Scoreboard()


'''
segments = [<turtle.Turtle object at 0x00000125167A9310>, 
<turtle.Turtle object at 0x00000125167A9100>, 
<turtle.Turtle object at 0x00000125167A9250>]
'''

# onkey() method allows you to trap keystrokes in order to perform special actions
# and in this case the functions we have bind to this are snake.up, snake.down,
# snake.left and snake.right
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)


game_is_on = True
while game_is_on:
    # The snake will show up only when the screen in  updated
    screen.update()
    # After every move the snake will pause for 0.1 seconds because otherwise it will
    # move at an unreasonable fast speed.
    time.sleep(0.1)
    snake.move()

    # collision with food
    # If the distance between the snake and the food is less than 15,
    # then call the refresh method and the food will move to another
    # random location.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase_length_of_snake()
        score.increase_score()

    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
            snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        # If we don't reset the snake then it will
        # keep moving in that direction
        snake.reset()

    # collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


# We used this so that the screen does not gets closed as soon as the
# program is executed.
screen.exitonclick()



