from turtle import Screen, Turtle
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270
class Snake:


    def __init__(self):
        self.snake1 = Turtle()
        self.snake2 = Turtle()
        self.snake3 = Turtle()
        self.snakes = [self.snake1, self.snake2, self.snake3]
        self.pos_x = 0
        self.pos_y = 0

        self.snake_create()

    def snake_create(self):
        for snake in self.snakes:
            snake.shape("square")
            snake.fillcolor("white")
            snake.penup()
            snake.goto(self.pos_x, self.pos_y)
            self.pos_x -= 20



    def snake_move(self, step):
        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.snakes[0].forward(step)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)


    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)


    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)


    def add_segment(self):
        num_of_seg = len(self.snakes)
        new_seg = Turtle()
        actual_x = self.snakes[num_of_seg-1].xcor()
        actual_y = self.snakes[num_of_seg-1].ycor()
        self.snakes.append(new_seg)
        new_seg.shape("square")
        new_seg.fillcolor("white")
        new_seg.penup()
        self.snakes[len(self.snakes)-1].goto(actual_x, actual_y)

    def check_collision(self):
        snake_without_head = self.snakes[1:len(self.snakes)]
        for snake in snake_without_head:
            if self.snakes[0].distance(snake) < 10:
                return True



