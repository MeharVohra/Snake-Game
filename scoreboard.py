from turtle import Turtle
ALIGN = "center"
MOVE = False
FONT = ("arial", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.score = 0
        # Instead of initializing high score with a number i.e.,
        # self.high_score = 0, we will open the created file "data.txt",
        # read the data which is in the form of a string and then convert
        # it to an integer and finally initialize to self.high_score
        with open("data") as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        # use the clear method so that whenever the score is increased it does
        # not overlap with other scores
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, move=MOVE, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Now we are going to update the high score by opening the file,
            # keeping the mode to write and then write the high score as a string
            with open("data", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align="center", move=False, font=("arial", 12, "normal"))
