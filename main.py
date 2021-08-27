from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Bem-vindo a Corrida de Tartarugas")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    new_turtle.goto(x=-238, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Faça a sua aposta", prompt="Qual tartaruga vai ganhar a corrida? Insira uma cor; ")

if user_bet:
    is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 220:
                is_race_on = False
                winning_color = turtle.pencolor()
                win_turtle = Turtle()
                if winning_color == user_bet:
                    win_turtle.color(winning_color)
                    style = ("Courier", 10)
                    win_turtle.write(f"Você venceu! A tartaruga {winning_color} é a vencedora", font=style, align="center")
                    win_turtle.hideturtle()
                    print(f"Você venceu! A tartaruga {winning_color} é a vencedora")
                else:
                    win_turtle.color(winning_color)
                    style = ("Courier", 10)
                    win_turtle.write(f"Você perdeu! A tartaruga {winning_color} é a vencedora", font=style, align="center")
                    win_turtle.hideturtle()
                    print(f"Você perdeu! A tartaruga {winning_color} é a vencedora")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
screen.exitonclick()
