from turtle import Turtle, Screen


class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score = {self.score}", align="center", font=('Arial', 24, 'normal') )
        self.screen = Screen()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=('Arial', 24, 'normal') )

    def update(self):
        self.color("white")
        self.clear()
        self.write(f"Score = {self.score}, High score = {self.high_score}", align="center", font=('Arial', 24, 'normal') )

    def get_highscore(self):
        with open("highscore.txt", mode="r") as file:
            high_score = file.read()
            self.high_score = int(high_score)


    def save_highscore(self):
        with open("highscore.txt", mode="w") as file:
            if self.score > self.high_score:
                self.high_score = self.score
                file.write( str(self.high_score))


#{"player": "player1", "score":0}