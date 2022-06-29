from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
snake = Snake()
screen = Screen()
food = Food()
screen.tracer(0)
screen.listen()
game_is_on = True
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
scoreboard = Score()


while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.snake_move(20)
    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.add_point()

    if snake.snakes[0].xcor() > 285 or snake.snakes[0].ycor() > 280 or snake.snakes[0].xcor() < -285 or snake.snakes[0].ycor() < -280:
        scoreboard.game_over()
        game_is_on = False
    if snake.check_collision():
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

