from turtle import Turtle

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score = {self.score}", align="center", font=('Arial', 24, 'normal') )

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=('Arial', 24, 'normal') )

    def game_over(self):
        self.color("white")
        self.clear()
        self.write("Game over", align="center", font=('Arial', 24, 'normal'))
        self.goto(0,200)
        self.write(f"Score = {self.score}", align="center", font=('Arial', 24, 'normal') )