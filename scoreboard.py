from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_num=1
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f"Level {self.level_num} " ,False, align='left', font=FONT)


    def increase_level(self):
        self.clear()
        self.level_num+=1
        self.update_level()