from turtle import Screen, Turtle
import time

screen  = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

# first step : Create a snake body
starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []
for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup() # 뱀이 움직일 떄 흰 선이 만들어지지 않게
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(2, 0, step= -1)





screen.exitonclick()

# Second step : Move the snake