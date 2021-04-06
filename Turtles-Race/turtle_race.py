import turtle
import random

width = 1000
height = 500

colors = ["blue", "green", "red", "brown", "orange", "pink", "purple", "black", "lightblue", "yellow"]


wn = turtle.Screen()
wn.setup(width, height)

class My_Turtle:

    rank = 1

    def __init__(self, color, player):
        self.color = color
        self.my_turtle = turtle.Turtle()
        self.my_turtle.color(color)
        self.my_turtle.shape("turtle")
        self.player = player


    def move_to_start(self, i):
        self.my_turtle.penup()
        self.my_turtle.goto(-width//2 + (width//(num_of_racers + 1)) * (i+1), -220)
        self.my_turtle.left(90)
        self.my_turtle.pendown()




def race(turtles_list):
    run = True
    while run:
        for current_turtle in turtles_list:
            if current_turtle.my_turtle.ycor() > 249:
                continue
            else: 
                current_turtle.my_turtle.ycor() <= 249
                current_turtle.my_turtle.forward(random.randint(0, 6))   
                if current_turtle.my_turtle.ycor() > 249:
                    print(current_turtle.player + f" has gotten rank {My_Turtle.rank}")
                    My_Turtle.rank += 1 

        if My_Turtle.rank == len(turtles_list) + 1:
            run = False


num_of_racers = turtle.numinput("Number of Turtles", "How many turtles would you like to race? (Max 10)", 
                                minval=1, maxval=10)

turtles_list = []

for i in range(int(num_of_racers)):

    turtles_list.append(My_Turtle(colors[i], f"Player {i + 1}"))
    turtles_list[i].move_to_start(i)


race(turtles_list)

wn.exitonclick()

